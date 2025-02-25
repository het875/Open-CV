import cv2 
import cv2 as cv 

img = cv.imread('Photos/cat.jpg')

# cv.imshow('cat image' , img)


# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue , frame = capture.read()

#     cv.imshow('Video' , frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# cv.waitKey(0)

img1 = cv2.resize(img,(560,700))
cv2.imshow("converted image==",img1)


k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()
    
elif k == ord("s"):
    cv2.imwrite("D:\\Open CV & LLM\\Open CV\\ouput.png",img1)  #it accept name of image and data
    cv2.destroyAllWindows()
