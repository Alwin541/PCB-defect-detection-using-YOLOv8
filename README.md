# PCB-defect-detection-using-YOLOv8
YOLOv8 model to detect pcb defects such as short circuit,mouse bite ,missing hole,open circuit,spurious copper in real time
🖥️ PCB Defect Detection using YOLOv8

This project focuses on detecting defects in Printed Circuit Boards (PCBs) using the YOLOv8 deep learning model. The system can automatically identify common PCB defects such as:

🔴 Mouse Bite

🔴 Short Circuit

🔴 Missing Hole

🔴 Spurious Copper

🔴 Open Circuit

🔴 Missing Component

🔴 Others (based on dataset annotations)

The goal is to support real-time defect detection for PCB quality inspection in manufacturing lines.

📌 Features

✅ YOLOv8-based object detection model

✅ Detects multiple PCB defect types in real-time

✅ Custom dataset training and evaluation

✅ Supports deployment on edge devices (e.g., Raspberry Pi, Jetson Nano)

✅ Easy-to-use inference pipeline with image/video inputs

✅ Extensible for new defect categories

📂 Project Structure
├── data/                  # Dataset (images + annotations in YOLO format)
├── runs/                  # Training logs and results
├── models/                # Pretrained and trained YOLOv8 models
├── notebooks/             # Jupyter notebooks for training & EDA
├── scripts/               # Training & inference scripts
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── app.py                 # (Optional) Inference app / demo

⚙️ Installation

#Install dependencies

pip install -r requirements.txt
Install YOLOv8 (Ultralytics)
pip install ultralytics
