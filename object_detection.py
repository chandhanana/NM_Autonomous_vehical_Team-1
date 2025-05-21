# Install YOLOv5 dependencies first
# pip install torch torchvision opencv-python

import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load YOLOv5s model
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated = results.render()[0]
    cv2.imshow('YOLOv5 Detection', annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
