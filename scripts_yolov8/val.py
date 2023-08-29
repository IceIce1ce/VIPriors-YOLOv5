from ultralytics import YOLO
from ultralytics.vit import RTDETR

#model = YOLO('runs/detect/yolov8m/weights/best.pt')
model = RTDETR("runs/detect/rtdetr-x/weights/best.pt")
metrics = model.val(data='DelftBikes.yaml', imgsz=640, batch=2, save_json=True, device=0, split='test', half=True)
metrics.box.map
metrics.box.map50
metrics.box.map75
metrics.box.maps
