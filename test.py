import os
os.system('python yolov5/detect.py --weights yolov5/runs/train/exp/weights/last.pt --img 640 --conf 0.25 --source 0')