import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('./paint1.jpeg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

gray1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Gray histogram

gray_hist = cv.calcHist([gray1], [0], None, [256], [0,256]) # calcHist(images, channels, mask, histSize, ranges)
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()



cv.waitKey(0)
# cv.destroyAllWindows()