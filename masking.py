import cv2 as cv 
import numpy as np



img=cv.imread('Images/puppy3.jpg')
cv.imshow('Original',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank image',blank)
#mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
#cv.imshow('Mask',mask)
weird_shape=cv.bitwise_and(circle,rectangle)
cv.imshow('Weird_Shape',weird_shape)


masked=cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Masked Image',masked) 
cv.waitKey(0)