import cv2 as cv 
img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

def changeRes(width,height):
    # For Live Videos Resizing
    capture.set(3,width)
    capture.set(4,height)



def rescaleFrame(frame,scale=0.75):
    # For images and videos.
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('Videos/dog.mp4')





while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
capture.release()
cv.destroyAllWindows()