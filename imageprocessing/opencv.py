import cv2
import numpy as np



while(1):
	frame = cv2.imread('plane.jpg')
	#img2 = img.astype(np.float32)
	#print(img2.dtype)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower = np.array([0,100,200])
	upper = np.array([30,255,255])

	mask = cv2.inRange(hsv, lower, upper)

	res = cv2.bitwise_and(frame,frame, mask= mask)

	cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
	cv2.resizeWindow('frame', 600,600)

	cv2.namedWindow('res',cv2.WINDOW_NORMAL)
	cv2.resizeWindow('res', 600,600)

	cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	cv2.imshow('res',res)

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