from flask import Flask, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# Load YOLO model
model = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Run YOLO detection
        results = model(frame)

        # Draw boxes
        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
