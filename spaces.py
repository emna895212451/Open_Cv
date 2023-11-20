from turtle import bgcolor
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Images/cat2.jpg')
cv.imshow('Original',img)

#plt.imshow(img)
#plt.show()

#  BGR to GRAYSCALE

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale',gray)

# BGR to HSV
HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',HSV)

# BGR to LAB(L*a*b)
LAB = cv.cvtColor(img,cv .COLOR_BGR2LAB)
cv.imshow('LAB',LAB)

# BGR to RGB 

rgb =cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
""" plt.imshow(rgb)
plt.show() """

# HSV to BGR
hsv_bgr=cv.cvtColor(HSV,cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR',hsv_bgr)

#LAB to BGR

lab_bgr=cv.cvtColor(LAB,cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR',lab_bgr)

cv.waitKey(0)  