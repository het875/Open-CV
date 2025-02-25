import cv2 as cv 

vd = cv.VideoCapture("Videos/dog.mp4")

while True:
    ret,frame = vd.read()
    cv.imshow("frame",vd)
    cv.waitKey(0)

vd.release()
cd.destroyAllWindows()