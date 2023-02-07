#!/usr/bin/python3
import cv2

video = cv2.VideoCapture(0)
#video = cv2.VideoCapture('gst-launch-1.0 v4l2src device=/dev/video0 ! xcimagesink')
#video = cv2.VideoCapture("gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, width=640, height=480 ! videoconvert ! video/x-raw,format=BGR ! appsink")
if not video.isOpened():
    print("Cannot open camera")
    for b in cv2.videoio_registry.getBackends():
        print(cv2.videoio_registry.getBackendName(b))
    exit()
#video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = cv2.QRCodeDetector()
frame = None
i = 0
cv2.namedWindow("preview")
#cv2.resizeWindow("preview", 1920, 1080)
while True:
    ret, frame = video.read()
    if not ret:
        print("Cannot receive frame")
        exit()

    cv2.imshow("preview", frame)
    cv2.waitKey(25)

    qrData = detector.detectAndDecode(frame)[0]
    if qrData :
        print( "Data detected: %s", qrData )
        break

video.release()
