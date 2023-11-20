import cv2 as cv
def rescaleframe(frame,scale=0.75):
    # work for images, videos and live videos
    width=int(frame.shape[1]*scale) # width=frame.shape[1]: the original width 
    height=int(frame.shape[0]*scale) #height=frame.shape[0] : the original height 
    dimentions=(width , height)
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)


#resizing images:

img = cv.imread('Images/puppy1.jpg')
resized_Image1=rescaleframe(img)
resized_Image2=rescaleframe(img,scale=5)
cv.imshow('Image1', resized_Image1)
cv.imshow('Image2', resized_Image2)




#resizing videos:
capture = cv.VideoCapture('Videos/MV.mp4')
while(True):
    isTrue,frame = capture.read()
    frame_resized1=rescaleframe(frame)
    frame_resized2=rescaleframe(frame,scale=.2)
    frame_resized3=rescaleframe(frame,scale=2)
    cv.imshow('Videos',frame)
    cv.imshow('Vedio resized1',frame_resized1)
    cv.imshow('Vedio resized2',frame_resized2)
    cv.imshow('Vedio resized3',frame_resized3)
    if cv.waitKey(20) &  0xFF ==ord('m'):
        break
capture.release()
cv.destroyAllWindows()





def changeRes(width,height):
    #only work for live videos
    capture.set(3,width)
    capture.set(4,height)
