from ultralytics import YOLO
from ultralytics.vit import RTDETR

#model = YOLO('yolov8l.yaml').load('yolov8l.pt')
#model.train(data='DelftBikes.yaml', epochs=80, imgsz=640, batch=1, name='yolov8m', plots=True)
model = RTDETR("runs/detect/rtdetr-x/weights/last.pt")
model.train(data='DelftBikes.yaml', epochs=100, imgsz=640, batch=8, name='rtdetr-x1', plots=True)
