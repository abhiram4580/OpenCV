import cv2 as cv 
import numpy as np 

# Generating a blank image.
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

# # 1. Paint an image with certain color
# blank[:]=0,0,255
# cv.imshow('Green',blank)

# 2. Drawing a Rectangle.
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)

# 3.Drawing a Circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)

# 4.Writing Text on an image.
cv.putText(blank,'Hello Abhiram',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)



#  5.Drawing a line.
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.imshow('Line',blank)
cv.waitKey(0)