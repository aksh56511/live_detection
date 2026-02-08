# Live Object Detection System

A real-time object detection application using YOLOv8 and Flask for web-based streaming and OpenCV for local camera feed.

## Overview

This project implements live object detection using the YOLOv8 (You Only Look Once) model. It provides two ways to visualize detections:
1. **Web Interface**: Stream live detection results through a Flask web server
2. **Desktop Application**: Direct camera feed with detection visualization using OpenCV

## Features

- ✅ Real-time object detection using YOLOv8n (nano model)
- ✅ Web-based streaming interface
- ✅ Standalone desktop application
- ✅ Efficient detection with bounding boxes and labels
- ✅ Support for 80+ object classes (COCO dataset)
- ✅ Low latency performance

## Requirements

- Python 3.8+
- Webcam/Camera device
- Dependencies:
  - Flask
  - OpenCV (cv2)
  - Ultralytics YOLO
  - PyTorch (installed with ultralytics)

## Installation

1. **Clone or download this repository**

2. **Install required packages:**
   ```bash
   pip install flask opencv-python ultralytics
   ```

3. **Verify YOLOv8 model:**
   - The `yolov8n.pt` file should be in the project root
   - If missing, it will be automatically downloaded on first run

## Usage

### Method 1: Web Interface (app.py)

Run the Flask web server:
```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

The web interface will display the live camera feed with object detection annotations.

**To stop:** Press `Ctrl+C` in the terminal

### Method 2: Desktop Application (yolo_test.py)

Run the standalone OpenCV application:
```bash
python yolo_test.py
```

A window will open showing the camera feed with real-time detections.

**To stop:** Press the `q` key

## Project Structure

```
live_detection/
│
├── app.py                 # Flask web server for streaming detection
├── yolo_test.py          # Standalone OpenCV detection script
├── yolov8n.pt            # YOLOv8 nano model weights
├── templates/
│   └── index.html        # Web interface template
└── README.md             # This file
```

## Technical Details

### YOLOv8n Model
- **Model:** YOLOv8 Nano (smallest and fastest variant)
- **Classes:** 80 object categories from COCO dataset
- **Performance:** Optimized for real-time detection
- **Input:** Live webcam feed (default camera index 0)

### Flask Application (app.py)
- **Framework:** Flask web framework
- **Endpoint:** Root `/` serves video stream
- **Port:** 5000 (accessible from network)
- **Format:** MJPEG streaming

### Desktop Application (yolo_test.py)
- **Library:** OpenCV for camera capture and display
- **Display:** Native window with annotations
- **Control:** Press 'q' to quit

## Detected Object Classes

The YOLOv8 model can detect 80 different object classes including:
- People
- Vehicles (car, truck, bus, motorcycle, bicycle)
- Animals (dog, cat, bird, horse, etc.)
- Common objects (phone, laptop, book, bottle, etc.)
- Furniture and household items
- And many more...

## Troubleshooting

**Camera not found:**
- Ensure your webcam is connected and not in use by another application
- Try changing camera index in code (0 to 1 or 2)

**Slow performance:**
- Close other resource-intensive applications
- Consider using a GPU if available (CUDA support)
- YOLOv8n is already the fastest variant

**Import errors:**
- Reinstall packages: `pip install --upgrade flask opencv-python ultralytics`

## Configuration

### Change Camera Source
Edit the camera index in both files:
```python
camera = cv2.VideoCapture(0)  # Change 0 to 1, 2, etc.
```

### Change Server Port (app.py)
Modify the port in the last line:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port number
```

## License

This project uses YOLOv8 from Ultralytics, which is licensed under AGPL-3.0.

## Credits

- **YOLOv8:** [Ultralytics](https://github.com/ultralytics/ultralytics)
- **Framework:** Flask, OpenCV
- **Model:** COCO pre-trained weights

## Future Enhancements

- [ ] Add recording functionality
- [ ] Implement object tracking
- [ ] Add detection confidence threshold controls
- [ ] Support for custom trained models
- [ ] Multiple camera support
- [ ] Detection history and analytics

---

**Note:** Ensure you have proper permissions to access the camera device on your system.
