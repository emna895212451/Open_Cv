import cv2 as cv


#showing images
img = cv.imread('Images/puppy1.jpg')
cv.imshow('Puppy',img)
cv.waitKey(0)#wait for infinate time
#cv.waitKey(1000)#wait for one second



#reading videos

capture = cv.VideoCapture('Videos/MV.mp4')
while(True):
    isTrue,frame = capture.read()
    cv.imshow('Videos',frame)
    if cv.waitKey(20) &  0xFF ==ord('m'):
        break
capture.release()
cv.destroyAllWindows()

#reading live videos 
capture = cv.VideoCapture(0)
while(True):
    isTrue,frame = capture.read()
    cv.imshow('Vedio ',frame)
    if cv.waitKey(20) &  0xFF ==ord('d'):
        break
capture.release()
cv.destroyAllWindows()