from ultralytics import YOLO
import sys
sys.path.append('/home/vip/harry/yolov11')
import cv2

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv11 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
