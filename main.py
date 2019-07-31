# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import cv2

# initialize the video stream and allow the camera sensor to warm up
vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=False).start()

# Variable to catch the barcode
found = set()
barcode_number = 0

# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it to have a maximum width of 480 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=480)

    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)
    
    # loop over the detected barcodes
    for barcode in barcodes:
		# extract the bounding box location of the barcode and draw the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
 
		# if the barcode text is currently not in our CSV file, write the timestamp + barcode to disk and update the set
        if barcodeData not in found:
            barcode_number = barcodeData
            found.add(barcodeData)

    # show the output frame
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF

    if barcode_number != 0:
        break

print(barcode_number)
# csv.close()
cv2.destroyAllWindows()
vs.stop()