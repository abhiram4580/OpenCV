import cv2 as cv 

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

 # Simple Thresholding 
threshold,thresh1=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Thresholded_image',thresh1)

#Inverse thresholded image.
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Thresholded_image',thresh)

# Adaptive Threshold 
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,5)
cv.imshow('Adaptive Thresholding',adaptive_thresh  )
 



cv.waitKey(0)