import cv2 as cv 
import numpy as np


blank  = np.zeros((500,500,3),dtype='uint8')# uint8 : data type of image // (500,500,3) = (height ,width , number of color chanal)
Blank1 =np.zeros((500,500,3),dtype='uint8')
Blank2 =np.zeros((500,500,3),dtype='uint8')
Blank3=np.zeros((600,600,3),dtype='uint8')
Blank4=np.zeros((600,600,3),dtype='uint8')
cv.imshow('Blank',blank)



#  1. paint the image a certain color 
blank[:]=0,255,0
blank[200:300,300:400]=0,0,255
blank[100:150,150:200]=255,0,0
cv.imshow('Green',blank)

# 2.draw a rectangle
Blank1[:]=150,150,0
cv.rectangle(Blank1,(0,0),(250,250),(0,255,0),thickness=2)
cv.rectangle(Blank1,(255,100),(400,400),(0,255,255),thickness=cv.FILLED)
cv.imshow('Rectangle',Blank1)
cv.rectangle(Blank2,(405,250),(460,450),(0,255,255),thickness=-1)
cv.rectangle(Blank2,(Blank2.shape[1]//2,Blank2.shape[0]//2),(400,400),(255,0,0),thickness=-1)
cv.rectangle(Blank2,(0,0),(Blank2.shape[1]//2,Blank2.shape[0]//2),(255,255,0),thickness=-1)
cv.imshow('Filled_rectangle',Blank2)

# 3.draw a circle

cv.circle(Blank3,(Blank3.shape[1]//2,Blank3.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Blank3',Blank3)

# 4.draw a line
cv.line(Blank3,(0,0),(Blank3.shape[1]//2,Blank3.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('Blank3',Blank3)


# 5. write text
cv.putText(Blank4,'Hello World',(225,225),cv.FONT_HERSHEY_PLAIN,1.0,(125,255,180),2)
cv.imshow('Text',Blank4)
cv.waitKey(0)