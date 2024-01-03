import cv2 as cv
import numpy as np

#img = cv.imread('./index2.jpeg', cv.IMREAD_GRAYSCALE)
blank = np.zeros((500,600,3),dtype='uint8')  # blank image
# cv.imshow("Blank", blank)

# 1. Paint the image a certain color 
blank[:] = 0,255,0   # Filled the blank image with green
# cv.imshow("Green", blank)

#cv.imshow("Image", blank)
# 2. Paint the image a certain region of color 
blank[200:300,300:400] = 255,0,0   # filled red color in the blank image on certain region(200:300,300:400)
# cv.imshow("Green", blank)

# 3. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2) # rectangle(start_point, end_point, color, thickness)
cv.rectangle(blank, (250,250), (450,450), (0,0,25), thickness=2)
# cv.imshow("Rectangle", blank)

# 4. Draw a circle 
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=3) # circle(center, radius, color, thickness)
# cv.imshow("Circle", blank)

# 5. Draw a circle with filled in
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1) # circle(center, radius, color, thickness) 
# cv.imshow("Circle", blank) 

# 6. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3) # line(start_point, end_point, color, thickness)
# cv.imshow("Line", blank)

# 7. Draw a circle filled in by using cv.FILLED
cv.circle(blank, (400,400), 50, (0,0,25), cv.FILLED)
# cv.imshow("Circle", blank)

# 8. Write text
cv.putText(blank, "Hello", (400,200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2) # putText(img, text, org, font, fontScale, color, thickness)
cv.imshow("Text", blank)

cv.waitKey(0)
cv.destroyAllWindows()