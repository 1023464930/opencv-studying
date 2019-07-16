# -*- coding: utf-8 -*-

import numpy as np
import cv2


cv2.namedWindow("CaptureFace")

cap = cv2.VideoCapture(0)
classfier = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")
color = (0, 255, 0)
while cap.isOpened():
    read, frame = cap.read()
    if not read:
        break
    # 灰度转换
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 人脸检测
    Rects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    if len(Rects) > 0:
        for Rect in Rects:
            x, y, w, h = Rect
            halfw = int(w/2)
            halfh = int(h/2)
            print(x+w/2, y+h/2)
            cv2.line(frame, (x + halfw, y - 30 + halfh), (x + halfw, y + 30 + halfh), (255, 0, 0), 2)
            cv2.line(frame, (x - 30 + halfw, y + halfh), (x + 30 + halfw, y + halfh), (255, 0, 0), 2)

    cv2.imshow("CaptureFace", frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
# 释放相关资源
cap.release()
out.release()
cv2.destroyAllWindows()
