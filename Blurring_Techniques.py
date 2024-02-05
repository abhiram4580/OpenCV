import cv2 as cv 

img=cv.imread('Photos/park.jpg')

# Averaging Blur
average=cv.blur(img,(7,7))
cv.imshow('Average Blur',average)

# Gaussian Blur
gaussian=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gaussian)

# Median Blur 
median=cv.medianBlur(img,3)
cv.imshow('Median',median)

# Bilateral Blur
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral)

cv.imshow('Image',img)
cv.waitKey(0)