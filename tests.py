import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
# read QR code
# read = decode(Image.open('qrcode.png'))
# print(read[0].data)


# generate QR code

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)

qr.add_data('Just some random text')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

img.save("sample.png")
