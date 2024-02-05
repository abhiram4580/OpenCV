import cv2 as cv 
import numpy as np 

img=cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)

b,g,r=cv.split(img)

blank=np.zeros(img.shape[:2],dtype='uint8')

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('red',red)





cv.imshow('Blur',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

merged=cv.merge([b,g,r])
cv.imshow('Merged_image',merged)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)
cv.waitKey(0)