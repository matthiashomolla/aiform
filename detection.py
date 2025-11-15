import cv2
from ultralytics import YOLO

# Load the image
frame = cv2.imread("frames/sample_2_first_frame.jpg")  # replace with actual filename

# Load YOLO model
model = YOLO("yolov8m.pt")

# Run detection
results = model(frame)

# Access bounding boxes
for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    score = box.conf[0]
    print(f"Player at [{x1}, {y1}, {x2}, {y2}] with confidence {score}")

    # INSERT_YOUR_CODE
    # Draw the bounding box on the image
    cv2.rectangle(frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
    # Optionally, draw the confidence score
    label = f"{score:.2f}"
    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    # Save the image
    cv2.imwrite("frames/sample_detection_frame.jpg", frame)
    print(f"Detection saved to frames/sample_detection_frame.jpg")
