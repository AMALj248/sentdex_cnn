import cv2
import numpy as np
import matplotlib.pyplot as plt

#Loading the image as GrayScale
img = cv2.imread('images/omega.jpg' , cv2.IMREAD_GRAYSCALE)

#Showing the image on matplotlib
plt.imshow(img , cmap='gray',interpolation='bicubic')
#plt.show()

#Showing the image on CV2
cv2.imshow('omega' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Saving an image
cv2.imwrite('saved.jpg' , img)

#Capturuing a Video Feed
cap = cv2.VideoCapture(0)

#Infinite Loop for video
while  True:
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    #To exit the videos and it checks for q press
    if cv2.waitKey(1) & 0xFF == ord('q') :
      break

#To Relase the camera anc close windows
cap.release()
cv2.destroyAllWindows()