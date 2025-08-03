import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("✅ Webcam is working!")
else:
    print("❌ Cannot access webcam. Try index 1 or 2.")

cap.release()
