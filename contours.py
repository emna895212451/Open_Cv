import cv2 as cv 
import  numpy as np

img = cv.imread('Images/cat3.jpg')

cv.imshow('Original',img)

blank = np.zeros(img.shape,dtype='uint8')
blank2 = np.zeros(img.shape,dtype='uint8')


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
blur=cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny) 
retval, threshold = cv.threshold(gray, 125, 255,cv.THRESH_BINARY) # thresholding ==> convert everything to white or black

cv.imshow('Threshold',threshold)
contours,hierarchies=cv.findContours(threshold ,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) # RETR_LIST : return all the contours on the images 
contours2,hierarchies=cv.findContours(canny ,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f' {len(contours)} contour(s) found!(with threshold methode)') 
print(f' {len(contours2)} contour(s) found!(with canny methode)') 
cv.drawContours(blank,contours,-1,(0,0,255),1)#-1 index : all of the contours  // 2 : thikness
cv.drawContours(blank2,contours2,-1,(255,0,0),1)
cv.imshow('Contours Drawing (threshold) ',blank)
cv.imshow('Contours Drawing (canny)',blank2)
cv.waitKey(0)