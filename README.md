# Human Action Recognition in Telehealth

A deep learning–based **Human Action Recognition (HAR)** system designed for telehealth environments.  
This project detects simple human movements and actions using a **CNN + LSTM architecture**, supported by a custom synthetic dataset of 15 videos.

It demonstrates how AI can be used in remote healthcare to monitor patient activity, identify movements, and support automated alerts without continuous human supervision.

---

## 🧠 Project Overview

Traditional telehealth systems lack real-time action monitoring.  
This project addresses that by providing:

- A lightweight action-recognition model  
- Clean preprocessing pipeline  
- A synthetic dataset for training/testing  
- Training, inference, and evaluation scripts  
- Modular, production-ready folder structure  

Built for students, researchers, and ML beginners looking to understand HAR.

---

## 🚀 Features

- Custom dataset of **15 synthetic action videos**:
  - Stick-figure walking  
  - Silhouette exercise actions  
  - Synthetic moving shapes  

- Automated **frame extraction**  
- CNN backbone + LSTM temporal modeling  
- Inference script to test any video  
- Annotation CSV for dataset labeling  
- Modular code structure for easy extension  

---

## 📂 Project Structure
human-action-recognition-telehealth/
│
├── src/
│ ├── preprocess.py # Extract frames from videos
│ ├── train.py # Train CNN-LSTM model
│ └── infer.py # Run inference on new videos
│
├── models/
│ └── simple_cnn_lstm.py # CNN + LSTM architecture
│
├── examples/
│ ├── sample_video.mp4
│ └── videos/
│ ├── synthetic/
│ ├── stick_walk/
│ └── silhouette_exercise/
│
├── annotations.csv # Video → label mapping
├── requirements.txt
├── LICENSE
└── README.md

