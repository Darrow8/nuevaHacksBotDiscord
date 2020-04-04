import pyqrcode
import os, sys
from IPython.display import Image
import png
from pyqrcode import QRCode
s = "nuevahacks.com/"

# Generate QR code
url = pyqrcode.create(s)

# url.svg("myqr.svg", scale = 1)
# url.png("yourqr.png",scale=8,module_color=[0,0,0,255],background=[255,255,255,255],quiet_zone=4)

img = url.png("qr.png",scale=8,module_color=[0,0,0,255],background=[255,255,255,255],quiet_zone=4)
# Image(filename="qr.png")