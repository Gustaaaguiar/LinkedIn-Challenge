# read qrcode

import cv2
import os

os.chdir('output/qrcode')

img = cv2.imread("#66743.png")
det = cv2.QRCodeDetector()
val, pts, st_code = det.detectAndDecode(img)
print(val)
