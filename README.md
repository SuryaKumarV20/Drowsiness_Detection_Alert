# 🛑 Driver Drowsiness Detection with Sound Alerts

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![Dlib](https://img.shields.io/badge/dlib-19.x-orange.svg)](http://dlib.net/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A real-time Python-based system that monitors a driver’s eye and mouth behavior using webcam input. It detects signs of drowsiness using **EAR (Eye Aspect Ratio)** and **MAR (Mouth Aspect Ratio)** and issues **sound alerts** when the driver shows signs of fatigue like eye closure or yawning.

---

## 🚀 Features

- 👁️ Real-time face & eye tracking using dlib and OpenCV
- 📏 EAR & MAR-based drowsiness detection
- 🔊 Sound alert (alert.wav) when drowsiness is detected
- 🧠 Optional head pose estimation
- 💡 Modular and lightweight codebase

---

## 🖼️ Screenshots

> **Real-Time Detection Example**  
> ![Screenshot](screenshots/detection_example.png)

> *(Add your own screenshot to the `screenshots/` folder and name it `detection_example.png`)*

---

## ⚙️ Requirements

Install all dependencies using:

```bash
pip install -r Requirements.txt
