import cv2 as cv
import matplotlib.pyplot as plt



img = cv.imread('./index2.jpeg')

cv.imshow("Image", img)
cv.waitKey(0)


plt.imshow(img)
plt.show()


cv.destroyAllWindows()
