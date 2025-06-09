from ultralytics import YOLO

model = YOLO('yolov8n.yaml')

model.train(
    data='data.yaml',  
    epochs=100,
    imgsz=640,
    batch=16,
    name='yolov8',     
    device=0,                
)

best_model = YOLO('runs/train/yolov8/weights/best.pt')