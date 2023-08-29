from ultralytics import YOLO

model = YOLO('runs/detect/yolov8m/weights/best.pt')
source = '../tmp/datasets/DelftBikes/test/images'
model.predict(source, save=True, imgsz=640, conf=0.001, iou=0.6, augment=True, save_conf=True, save_txt=True, device=0, half=True)
