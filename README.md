# YOLO-series
YOLOv5 ~ v11 for Inference at Local & Jetson board


## Installation
<pre> <code> pip install ultralytics </code> </pre>
<pre> <code> pip install -r requirements.txt </code> </pre>

## yolov5 github
https://github.com/ultralytics/yolov5
### Inference using webcam
TBD

## yolov6 github
https://github.com/meituan/YOLOv6
### Inference using webcam
<pre> <code> python3 tools/infer.py --weights yolov6n.pt --source 0 --webcam --yaml data/coco.yaml --view-im </code> </pre>

## yolov7 github
https://github.com/WongKinYiu/yolov7
### Inference using webcam
<pre> <code> python3 detect.py --weights yolov7.pt --conf 0.25 --source 0 --view-img --view-im </code> </pre>

## yolov8 github
https://github.com/autogyro/yolo-V8
https://docs.ultralytics.com/ko/models/yolov8/
### Inference using webcam
<pre> <code> python3 infer.py --weights yolov8n.pt --conf 0.25 --source 0 --view-img --view-im </code> </pre>

## yolov9 github
https://github.com/WongKinYiu/yolov9
### Inference using webcam
<pre> <code> python3 detect.py --weights yolov9t.pt --conf 0.25 --source 0 --view-img </code> </pre>

## yolov10 github
https://github.com/THU-MIG/yolov10
### Inference using webcam
<pre> <code> python3 app.py --weights yolov10n.pt --conf 0.25 --source 0 --view-img </code> </pre>
and also connect to the link below
<pre> <code> http://127.0.0.1:7860 </code> </pre>

## yolov11 github
https://github.com/THU-MIG/yolov10
### Inference using webcam
<pre> <code> python3 infer.py --weights yolov11n.pt --conf 0.25 --source 0 --view-img </code> </pre>
