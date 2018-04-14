import cv2
import numpy as np
vs = cv2.VideoCapture(0)
if not(vs.isOpened()):
    vs.open()

if hasattr(cv2, 'cv'):
    vs.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 4416)
    vs.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1242)
else:
    vs.set(cv2.CAP_PROP_FRAME_WIDTH, 4416)
    vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 1242)
while True:
    ok, frame = vs.read()
    frame = frame[0:376, 0:650]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 100, 100])
    upper = np.array([5, 255, 255])
    lower2 = np.array([170, 100, 100])
    upper2 = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    mask2 = cv2.inRange(hsv, lower2, upper2)

    maskc = cv2.add(mask, mask2)

    res = cv2.bitwise_and(frame, frame, mask=maskc)

    im2, contours, hierarchy = cv2.findContours(maskc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
    if not contours:
        for c in contours:
            # compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # draw the contour and center of the shape on the image
            # cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            # cv2.circle(frame, (cX, cY), 7, (0, 255, 0), -1)
            # cv2.putText(frame, "center", (cX - 20, cY - 20),
            #			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.drawMarker(frame, (cX, cY), (0, 255, 0), markerSize=200, thickness=20)

    cv2.imshow("frame", frame)
    cv2.waitKey(2)
cv2.destroyAllWindows()
