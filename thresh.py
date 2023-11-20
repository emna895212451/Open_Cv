import cv2 as cv 


img=cv.imread('Images/cat3.jpg')
cv.imshow('Original',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Simple Threasholding

threshold,thresh =cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('simple Thresholded',thresh)

threshold,thresh_inv =cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('simple Thresholded  Inverse',thresh_inv)


#adaptive Thresholding 

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('Adaptive Threshholding',adaptive_thresh)

cv.waitKey(0)