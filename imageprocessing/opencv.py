import cv2
import numpy as np



frame = cv2.imread('photo12.jpg')
#img2 = img.astype(np.float32)
#print(img2.dtype)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower = np.array([0,100,100])
upper = np.array([5,255,255])
lower2 = np.array([170,100,100])
upper2 = np.array([180,255,255])

mask = cv2.inRange(hsv, lower, upper)
mask2 = cv2.inRange(hsv, lower2, upper2)

maskc = cv2.add(mask,mask2)

res = cv2.bitwise_and(frame,frame, mask= maskc)

im2, contours, hierarchy = cv2.findContours(maskc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key = cv2.contourArea, reverse = True)[:1]
for c in contours:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	# draw the contour and center of the shape on the image
	#cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
	#cv2.circle(frame, (cX, cY), 7, (0, 255, 0), -1)
	#cv2.putText(frame, "center", (cX - 20, cY - 20),
	#			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	cv2.drawMarker(frame,(cX, cY),(0, 255, 0),markerSize=200,thickness=20)
	print("hallo:" + str(cX) + " " + str(cY))
#print(contours.__len__())
#cv2.drawContours(im2, contours, 3, (0,255,0), 3)
#cv2.drawContours(im2, contours, -1,(0,0,255),3)

cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 600,600)

cv2.namedWindow('maskc',cv2.WINDOW_NORMAL)
cv2.resizeWindow('maskc', 600,600)

cv2.imshow('frame',frame)
cv2.imshow('maskc',maskc)
#cv2.imshow('res',res)
while(1):
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',hsv)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()
