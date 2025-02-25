# # Python code to read image
# import cv2 as cv , cv2 


# # To read image from disk, we use
# # cv2.imread function, in below method,
# # img = cv.imread('Photos/cat_large.jpg')
# img = cv2.imread("Photos/cat.jpg", cv2.IMREAD_COLOR)

# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# # Creating GUI window to display an image on screen
# # first Parameter is windows title (should be in string format)
# # Second Parameter is image array
# cv.imshow('Cat' , img)
# cv.imshow('Gray Image' , gray_image)

# # To hold the window on screen, we use cv2.waitKey method
# # Once it detected the close input, it will release the control
# # To the next line
# # First Parameter is for holding screen for specified milliseconds
# # It should be positive integer. If 0 pass an parameter, then it will
# # hold the screen until user close it.
# cv.waitKey(0)


# # It is for removing/deleting created GUI window from screen
# # and memory
# # cv2.destroyAllWindows()





import cv2 as cv 

img  = cv.imread('Photos/cat.jpg')

# gray_img = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# resized_img = cv.resize(img , (400,400))

# rectangle_img = cv.rectangle(img ,(50,50), (200,200), (0 , 50 , 0), 3 )

# circle_img = cv.circle(img, (450, 200), 150 , (0, 0, 255), 5)

# line_image = cv.line(img, (250, 50), (800, 800), (255, 0, 0), 2)



# cv.imshow("Cat Image with orgnal width and height" , img)

# cv.imshow("Gray Image" , gray_img)

# cv.imshow("Resized imagwe" ,  resized_img)

# cv.imshow("Rectangle img " , rectangle_img)

# cv.imshow("Circle image " , circle_img)

# cv.imshow("Line image " , line_image)



cv.waitKey(0)
cv.destroyAllWindows()


