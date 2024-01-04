import cv2 as cv
import matplotlib.pyplot as plt

# can be used for images, videos or webcam or live videos
'''
def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
'''
# can be used for only live videos or webcam
def changeRes(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)

#capture = cv.VideoCapture('video (2160p).mp4')
capture = cv.VideoCapture(0)


while True:
    ret,frame = capture.read()
    
    if not ret:
        break
    else:
        #frame_resized = rescaleFrame(frame)
        frame_resized = changeRes(capture, 640, 480)
        

       # cv.imshow("Video", frame)
        cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    
    
    
capture.release()
cv.destroyAllWindows()


