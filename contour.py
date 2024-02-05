import cv2 as cv 
import numpy as np 

img=cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("THRESH",thresh)

# canny=cv.Canny(img,125,175)
# cv.imshow('Canny Edges',canny)

contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank,contours,-1,(0,0,255))
cv.imshow('Contours Drawn',blank)

cv.imshow('CAT',gray)

cv.waitKey(0)
