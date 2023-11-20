from lib2to3.pgen2.token import CIRCUMFLEX
import cv2 as cv 
import numpy as np 

blank = np.zeros((400,400),dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)


#bitwise And 
betwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('Betwise_And',betwise_and)
#bitwise Or
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise_Or',bitwise_or)

#bitwise Not
bitwise_not_Circle=cv.bitwise_not(circle) 
cv.imshow('Bitwise_Not_Circle',bitwise_not_Circle)
bitwise_not_Rectangle=cv.bitwise_not(rectangle)
cv.imshow('Bitwise_Not_Rectangle',bitwise_not_Rectangle)
# bitwise Xor
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise_Xor',bitwise_xor)
cv.waitKey(0)
