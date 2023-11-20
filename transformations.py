from configparser import Interpolation
from turtle import width
import cv2 as cv 
import numpy as np




img=cv.imread('Images/cat2.jpg')
cv.imshow('Original',img)

#Translation

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
   # -x--> Left
   # -y--> Up
   # x --> Right
   # y --> Down
translated = translate(img,100,100)
cv.imshow('Translated',translated)


#Rotation 

def rotate(img,angle,rotpoint=None):
    (height,width) = img.shape[:2]


    if rotpoint == None :
        rotPoint=(width//2,height//2)

    rotMat= cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,-45)
cv.imshow('Rotated',rotated)
rotated_rotated= rotate(rotated,-90)
cv.imshow('Rotated_Rotated',rotated_rotated)
    
#Resizing 

resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)#shrinking the image : INTER_AREA , larging the image : INTER_Leanear or INTER_CUBIC
cv.imshow('Resized',resized)
rotated_resized= rotate(resized,-90)
cv.imshow('Rotated_Resized',rotated_resized)


#Flipping 

flip =cv.flip(img,-1) # flip(image,flip code) , flip code = 0 (fliping vertacly) or 1 (horizontaly) or -1 (both vertacly and horizontaly)
cv.imshow('Flip',flip)

# Cropping

cropped= img[200:400 , 300:600]
cv.imshow('Cropped',cropped)
cv.waitKey(0)