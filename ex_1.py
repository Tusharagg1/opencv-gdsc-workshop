import cv2

cap = cv2.VideoCapture('vid1.mp4')

cv2.namedWindow('Video file', cv2.WINDOW_NORMAL)  # resize window size to fit in the screen

ret, img = cap.read()  # read first frame in video #ret = return, tell if reading video was successful

while ret:
    cv2.imshow('Video file', img)

    cv2.waitKey(0)  # waitKey(0): it will wait for input from keyboard
    ret, img = cap.read()
