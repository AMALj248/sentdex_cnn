import numpy as np
import pandas as pd
import cv2

img = cv2.imread('images/omega.jpg' , cv2.IMREAD_COLOR)

#Refrencing a pixel color
px = img[55,55]

#Modification of a pixel
img[55,55] = [255,255,255]
print(px)

#ROI ->Region of a image
roi=img[100:150 , 100:150] = [255,255,255]
print(roi)

cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

