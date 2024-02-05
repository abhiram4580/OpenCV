import cv2 as cv 
import matplotlib.pyplot as plt 

img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)


# BGR to GrayScale.
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

# BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to LAB 
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# BGR to RGB 
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("LAB",rgb)

# HSV to BGR 
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)

plt.imshow(rgb)
plt.show()


cv.imshow('Park',img)
cv.waitKey(0)