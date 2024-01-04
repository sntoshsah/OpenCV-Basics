import cv2 as cv


cap = cv.VideoCapture('video (1080p).mp4') # 0 is the default camera

#error: (-215:Assertion failed) will return if path is not matched or frame ended


'''
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True: # if frame is read correctly, ret is True
        cv.imshow('Frame', frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print("Can't receive frame (stream end?). Exiting ...")
        break

'''
while True:
    ret,frame = cap.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...") 
        break

cap.release()
cv.destroyAllWindows()