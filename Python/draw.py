import cv2 as cv
import numpy as np

#img = cv.imread('./index2.jpeg', cv.IMREAD_GRAYSCALE)
blank = np.zeros((500,600,3),dtype='uint8') 
cv.imshow("Blank", blank)

# 1. Paint the image a certain color 
blank[:] = 0,255,0
cv.imshow("Green", blank)

#cv.imshow("Image", blank)
# 1. Paint the image a certain region of color 
blank[200:300,300:400] = 255,0,0
cv.imshow("Green", blank)

#2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow("Rectangle", blank)
cv.rectangle(blank, (250,250), (450,450), (0,0,25), thickness=2)
cv.imshow("Rectangle", blank)

# 3. Draw a circle 
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow("Circle", blank)

# 3. Draw a circle with filled in
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow("Circle", blank) 

cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), cv.fill)
cv.imshow("Circle", blank)


cv.waitKey(0)
cv.destroyAllWindows()