**# 👁️ Real-Time Face and Eye Detection using OpenCV**

An end-to-end Computer Vision project developed using Python and OpenCV to detect human faces and eyes in real time through a webcam. The project uses Haar Cascade Classifiers to identify facial features efficiently and displays the detection results with bounding boxes for easy visualization.

** 📘 Project Overview**
* The Real-Time Face and Eye Detection System is a computer vision mini-project developed using Python and OpenCV.
  It demonstrates real-time object detection through a live webcam feed using Haar Cascade Classifiers a machine learning-based method for visual object recognition.
  
* The system captures video frames, converts them into grayscale, and applies pre-trained cascades to detect human faces and eyes efficiently. 
  Detected objects are highlighted with color coded bounding boxes (green for faces and blue for eyes), and results are displayed live with smooth rendering.
  
* This project emphasizes accuracy, speed, and user-friendliness, achieved through optimized detection parameters and an intuitive visualization interface.
  It runs seamlessly both in Jupyter Notebook (for demonstration) and as a standalone Python script.
  
* The project provided hands-on experience in image processing, object detection, and real-time video analysis, showcasing how traditional algorithms can be used effectively in practical computer vision applications.

**🎯 Objectives**

- Detect human faces and eyes in real time using a webcam.
- Apply Haar Cascade Classifiers for object detection.
- Demonstrate practical Computer Vision techniques using Python.
- Provide a simple and efficient real-time detection system.

**🚀 Features**

Real-time detection of faces and eyes from webcam input.

Uses Haar Cascade Classifiers for efficient detection.

Displays bounding boxes with clear labels.

Adjustable parameters for better accuracy and performance.

Works in both Jupyter Notebook and command-line script modes.

Modular and easy to extend with other detectors or DNN models.


**🧰 Technologies Used**

| Category | Tools |
|----------|-------|
| Language | Python |
| Libraries | OpenCV, NumPy, Pillow |
| Development Environment | Jupyter Notebook / VS Code |
| Computer Vision | Haar Cascade Classifiers |



**📂 Folder Structure**

📁 realtime-face-eye-detection/
│
├── screenshots/
│
├── face_eye_detection.py
│
├── requirements.txt
│
├── README.md
│
├── LICENSE
│
└── .gitignore

**⚙️ Installation and Setup**

1. Clone the repository

```bash
git clone https://github.com/Viiddzzz/realtime-face-eye-detection.git
cd realtime-face-eye-detection
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python face_eye_detection.py
```



**🛠️ How It Works**

1.Captures frames from your system’s webcam.

2.Converts frames to grayscale for efficient processing.

3.Applies Haar Cascade Classifiers to detect faces.

4.Locates eyes within detected face regions.

5.Draws labeled bounding boxes and displays live results.

**🏁 Results**

- Successfully detects faces and eyes in real time.
- Displays bounding boxes around detected facial features.
- Provides smooth live detection using OpenCV.
- Demonstrates efficient implementation of Haar Cascade Classifiers.

**💼 Real-World Applications**

- Smart attendance systems
- Driver monitoring systems
- Face recognition preprocessing
- Human-computer interaction
- Surveillance and security systems


**🛠 Skills Demonstrated**

- Python Programming
- OpenCV
- Computer Vision
- Image Processing
- Haar Cascade Classifiers
- Real-Time Video Processing


**🌟 Future Enhancements**

1.Add Deep Learning (DNN)-based face detectors for better accuracy.

2.Integrate mask detection or emotion recognition.

3.Include a GUI for starting/stopping the camera feed.

4.Deploy as a small desktop or web app using Flask or Streamlit.


**🧑‍💻 Author**
Vidyashree S

Aspiring Data Analyst | Python & Computer Vision Enthusiast

📧 vidyaa1103@gmail.com

https://github.com/Viiddzzz/realtime-face-eye-detection

