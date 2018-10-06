import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])

    # define range of blue color in HSV
    lower_blue = np.array([0,100,100])
    upper_blue = np.array([20,255,255])


    # Threshold the HSV image to get only blue colors
    #Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar.

    #Python: cv2.bitwise_and(src1, src2[, dst[, mask]]) → dst


#Parameters:
#src1 – first input array or a scalar.
#src2 – second input array or a scalar.
#dst – output array that has the same size and type as the input arrays.
#mask – optional operation mask, 8-bit single channel array, that specifies elements of the output array to be changed.

    

    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
