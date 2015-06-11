from Transformation import Transformation
from FirePixelDetector import FirePixelDetector
import numpy as np
import cv2

class FireMask(Transformation):
	def transform(self, img):
		firePixelDetector = FirePixelDetector(img, 60, 125)
		shape = np.shape(img)
		mask = np.zeros((shape[0], shape[1]), np.uint8)

		for x in range(shape[0]):
			for y in range(shape[1]):
				if firePixelDetector.detect(x, y):
					mask.itemset((x, y), 1)
				else:
					mask.itemset((x, y), 0)

		# define range of fire color
		#lower_fire = np.array([0,60,160])
		#upper_fire = np.array([80,170,255])

		# Threshold the HSV image to get only fire colors
		#mask = cv2.inRange(img, lower_fire, upper_fire)

		# Gaussian blur + Otsu's method to decrease noise (might not be useful)
		#blur = cv2.GaussianBlur(mask,(5,5),0)
		#ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

		# Erode and Dilate filters blobs
		#kernel = np.ones((5,5), np.uint8)
		#erosion = cv2.erode(th3,kernel,iterations=1)
		#dilation = cv2.dilate(erosion,kernel,iterations=1)

		# Bitwise-AND mask and original image
		res = cv2.bitwise_and(img,img, mask=mask)
		return res