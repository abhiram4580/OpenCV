import cv2 as cv 
import numpy as np 

img=cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)

# Transalation 
def transalate(img,x,y):
    transMat=np.float32([[1,0,x],[1,0,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)


transalaated=transalate(img,10,10)
cv.imshow('Transalated',transalaated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
rotated1=rotate(rotated,-45)
cv.imshow('Rotated',rotated1)

## Resizing 
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

## Flipping an image
flip=cv.flip(img,0)
cv.imshow('Flipped',flip)

## Cropping an image 
cropped=img[200:400,500:600]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
