import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 


img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray_Scale_Iamge',gray)



#Grayscale Histogram 
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
cv.imshow('Gray',gray)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask',masked)


# plt.figure()
# plt.title('GrayScale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
# plt.plot(mask)
# plt.xlim([0,256])
# plt.show()


# Colour Histogram 

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')

colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([masked],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)