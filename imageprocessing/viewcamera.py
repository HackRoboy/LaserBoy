import cv2
vs = cv2.VideoCapture(0)
while True:
    ok, frame = vs.read()
    cv2.imshow("frame", frame)
    cv2.waitKey(0)