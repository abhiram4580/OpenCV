import cv2 as cv 

img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

# Gray
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# Blur 
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)

# Edge Cascade 
canny=cv.Canny(blur,125,175)
cv.imshow('canny Edges',canny)

# Dialating the images
dilate=cv.dilate(canny,(7,7),iterations=3 )
cv.imshow('Dialated',dilate)

# Eroding 
erode=cv.erode(dilate,(3,3),iterations=3)
cv.imshow('Erode',erode)

# Resizing 
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

# Cropping 
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)
