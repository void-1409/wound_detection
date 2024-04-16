from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(data="data.yaml", epochs=50)