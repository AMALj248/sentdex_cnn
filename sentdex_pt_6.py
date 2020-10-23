import numpy as np
import pandas as pd
import cv2

img=cv2.imread('images/low_light.jpg')
# retval , threshold1 = cv2.threshold(img , 12 , 255, cv2.THRESH_BINARY)
#
grayscaled = cv2.cvtColor(img  , cv2.COLOR_BGR2GRAY)
#
# retval2 , threshold2 = cv2.threshold(grayscaled , 12 , 255, cv2.THRESH_BINARY)
#
# cv2.imshow('Original' , img)
# cv2.imshow('Threshold1' , threshold1)
# cv2.imshow('Threshold2' , threshold2)

#Adaptive Threshold
gauss = cv2.adaptiveThreshold(grayscaled , 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY,155,1)
cv2.imshow('Gauss', gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()