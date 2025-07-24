import cv2
import cvzone
import numpy as np
import pandas as pd
from picamera2 import Picamera2
from ultralytics import YOLO

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
model = YOLO("best.pt")
my_file = open("mushroom.txt", "r", encoding="utf-8")
data = my_file.read()
class_list = data.split("\n")
COUNT = 0
while True:
    im = picam2.capture_array()

    COUNT += 1
    if COUNT % 3 != 0:
        continue
    im = cv2.flip(im, -1)
    results = model.predict(im)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    for index, row in px.iterrows():
        # print(row)

        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]

        cv2.rectangle(im, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cvzone.putTextRect(im, f"{c}", (x1, y1), 1, 1)
    cv2.imshow("Camera", im)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
