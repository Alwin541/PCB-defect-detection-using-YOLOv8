from ultralytics import YOLO
import cv2

# Load the YOLOv8 model (replace with your own .pt file)
model = YOLO("best (1).pt")

# Open webcam
cap = cv2.VideoCapture(0)  # Change to 1 if using external webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the frame
    results = model(frame)

    # Plot results
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv8 PCB Defect Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
