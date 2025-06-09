import argparse
from ultralytics import YOLO
import os
import cv2

import sys
sys.path.append('/home/vip/harry/yolov8')

def run_inference(weights, source, imgsz=640, conf=0.25, save=True, view_img=False):
    model = YOLO(weights)
    results = model.predict(
        source=source,
        imgsz=imgsz,
        conf=conf,
        save=save,
        stream=view_img
    )

    if view_img:
        for result in results:
            im = result.plot()
            cv2.imshow("YOLOv8 Inference", im)
            if cv2.waitKey(0 if isinstance(source, str) and os.path.isfile(source) else 1) == 27:
                break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, required=True, help='YOLOv8 모델 경로 (e.g., yolov8n.pt)')
    parser.add_argument('--source', type=str, required=True, help='이미지/폴더/비디오/웹캠 경로 (e.g., 0 또는 test.jpg)')
    parser.add_argument('--imgsz', type=int, default=640, help='입력 이미지 크기')
    parser.add_argument('--conf', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--nosave', action='store_true', help='결과 이미지 저장 안함')
    parser.add_argument('--view-img', action='store_true', help='OpenCV로 실시간 결과 보기')

    opt = parser.parse_args()
    run_inference(
        weights=opt.weights,
        source=opt.source,
        imgsz=opt.imgsz,
        conf=opt.conf,
        save=not opt.nosave,
        view_img=opt.view_img
    )

