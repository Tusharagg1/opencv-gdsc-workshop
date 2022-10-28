# blurring gets rid of the noise
import cv2

cap = cv2.VideoCapture('vid1.mp4')
cv2.namedWindow('Video file', cv2.WINDOW_NORMAL)
cv2.namedWindow('blurred', cv2.WINDOW_NORMAL)

# if we don't add anything after above statements,
# the program will open video file and close
# because it is done running the program,
# and it has nothing to do/run after.

ret, img = cap.read()  # reads only one frame (in this case, the first frame here)

while ret:
    blurred = cv2.GaussianBlur(img, (27, 27), 0)  # blur (27 x 27) pixels of window
    cv2.imshow('blurred', blurred)
    cv2.imshow('Video file', img)

    cv2.waitKey(10)
    ret, img = cap.read()
