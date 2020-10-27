import cv2
import numpy as np
#To capture Videos
cap = cv2.VideoCapture(0)

while True:
    #- is a necessary but useless value
    ret , frame = cap.read()
    #hue sarturation and value

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    #Selecrting color range
    lower_black = np.array([10,10,10])
    upper_black = np.array([255,255,255])

    #masking
    mask = cv2.inRange(hsv , lower_black , upper_black)
    res = cv2.bitwise_and(frame , frame , mask = mask)

    #Averaging
    kernel = np.ones((15,15) , np.float32)/225
    smoothed = cv2.filter2D(res , -1 , kernel)

    #median blur
    median = cv2.medianBlur(res,15)


    #Showing all the videos
    cv2.imshow('frame'  , frame)
    #cv2.imshow('mask' , mask)
    cv2.imshow('res' , res )
    cv2.imshow('median', median)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
#Realeasing the camera
cap.release()
