import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np

st.title("🔍 Real-Time PCB Defect Detection (YOLOv8)")

# Load YOLOv8 model
model = YOLO("best (1).pt")  # Replace with your model file

# Webcam toggle
run = st.checkbox("Start Webcam")

# Placeholder for webcam feed
frame_placeholder = st.empty()

# Open webcam (device 0)
cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        st.warning("Failed to grab frame from webcam.")
        break

    # Run YOLOv8 inference
    results = model(frame)
    annotated = results[0].plot()

    # Convert to RGB for Streamlit
    annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    # Display in Streamlit
    frame_placeholder.image(annotated_rgb, channels="RGB")

cap.release()
