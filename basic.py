import cv2 as cv


img =cv.imread('Images/puppy3.jpg')
cv.imshow('Puppy',img)

# Converting an image to grayscale

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur
blur =cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade

canny1 = cv.Canny(img,125,175)
canny2 = cv.Canny(blur,125,175)
canny3=cv.Canny(img,20,30)

cv.imshow('Canny Edges1',canny1)
cv.imshow('Canny Edges2',canny2)
cv.imshow('canny Edges3',canny3)

# Dilating the image
dilated = cv.dilate(canny2,(7,7),iterations=3)

cv.imshow('Dilated',dilated)

#Eroding
eroded =cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Croping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)


cv.waitKey(0)