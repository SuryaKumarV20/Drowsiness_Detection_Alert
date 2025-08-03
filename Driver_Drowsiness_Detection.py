import cv2
import dlib
from scipy.spatial import distance
import pygame
import threading

# ---------------------- Initialize Alert Sound ----------------------
pygame.mixer.init()
pygame.mixer.music.load("alert.wav")  # Make sure alert.wav is in the same folder

def play_alarm():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

# ---------------------- EAR (Eye Aspect Ratio) ----------------------
def calculate_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# ---------------------- Face Detector & Landmark Model ----------------------
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Ensure this file is present

# Eye landmark indexes (for left and right eye)
LEFT_EYE_POINTS = list(range(36, 42))
RIGHT_EYE_POINTS = list(range(42, 48))

# Thresholds
EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 20
counter = 0

# ---------------------- Start Video Stream ----------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        # Get left and right eye landmarks
        left_eye = []
        right_eye = []

        for i in LEFT_EYE_POINTS:
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            left_eye.append((x, y))
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        for i in RIGHT_EYE_POINTS:
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            right_eye.append((x, y))
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        # Compute EAR
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        ear = (left_ear + right_ear) / 2.0

        # Check if drowsy
        if ear < EAR_THRESHOLD:
            counter += 1
            cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

            if counter >= CONSEC_FRAMES:
                threading.Thread(target=play_alarm).start()
        else:
            counter = 0
            pygame.mixer.music.stop()

    cv2.imshow("Driver Drowsiness Detection", frame)
    if cv2.waitKey(1) == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
