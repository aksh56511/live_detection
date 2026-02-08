from ultralytics import YOLO
import cv2

# Load model (nano version = fastest)
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    # Draw detections
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
