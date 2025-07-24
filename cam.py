import cv2
import cvzone
import numpy as np
from picamera2 import Picamera2
from ultralytics import YOLO

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
model = YOLO("best.pt")
with open("mushroom.txt", "r", encoding="utf-8") as my_file:
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
    boxes = results[0].boxes.data
    if hasattr(boxes, 'cpu'):
        boxes = boxes.cpu().numpy()
    else:
        boxes = np.array(boxes)

    for row in boxes:
        x1, y1, x2, y2, _, d = row.astype("float")
        c = class_list[int(d)]
        cv2.rectangle(im, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
        cvzone.putTextRect(im, f"{c}", (int(x1), int(y1)), 1, 1)
    cv2.imshow("Camera", im)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
