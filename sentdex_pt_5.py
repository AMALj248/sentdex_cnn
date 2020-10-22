import numpy as np
import pandas as pd
import cv2

img0=cv2.imread('images/omega.jpg')
img1 = cv2.imread('images/img1.jpg')
img2 = cv2.imread('images/img2.jpg')

#additiom of images
#add = img1+img2
#CV2 operation
add=cv2.add(img1 , img2)
#Weighted Addition with Weights
weighted = cv2.addWeighted(img1,0.6 , img2 , 0.4 , 0)


rows , cols , channels = img0.shape
roi = img0[0:rows , 0:cols ]
#Masking the image
img2gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
#Tresholding
ret , mask = cv2.threshold(img2gray , 220 , 255 , cv2.THRESH_BINARY_INV)

#parts in balck
mas_inv = cv2.bitwise_not(mask)
img_bg = cv2.bitwise_and(roi , roi ,mask = mas_inv)
img2_fg = cv2.bitwise_and(roi , roi ,mask = mask)

dst = cv2.add(img_bg ,img2_fg )
img2[0:rows , 0:cols] = dst

cv2.imshow('combine' , img2)
cv2.waitKey(0)
cv2.destroyAllWindows()