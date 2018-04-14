import cv2
vs = cv2.VideoCapture(0)
while True:
    ok, frame = vs.read()
    frame = frame[0:376, 0:677]
    cv2.imshow("frame", frame)
    cv2.waitKey(2)