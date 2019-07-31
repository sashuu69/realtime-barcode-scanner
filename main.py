# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import datetime
import imutils
import time
import cv2

# initialize the video stream and allow the camera sensor to warm up
vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=False).start()

