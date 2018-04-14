import cv2
import numpy as np



while(1):
	frame = cv2.imread('photo1.JPG')
	#img2 = img.astype(np.float32)
	#print(img2.dtype)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower = np.array([-10,100,220])
	upper = np.array([10,255,255])

	mask = cv2.inRange(hsv, lower, upper)

	res = cv2.bitwise_and(frame,frame, mask= mask)

	cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
	cv2.resizeWindow('frame', 1000,1000)

	cv2.namedWindow('res',cv2.WINDOW_NORMAL)
	cv2.resizeWindow('res', 1000,1000)

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