import cv2 as cv

img =  cv.imread('Project/gettyimages-169710978-612x612.jpg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('Project/Haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) 
    cv.imshow('detected faces', img)
    
    
cv.waitKey(0)
cv.destroyAllWindows