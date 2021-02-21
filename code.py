import qrcode as qr

qr_code = qr.QRCode(
    version=1,
    box_size=5,
    border=2,
)

qr_code.add_data("Easy to build QR code")
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="white")
img.save('image.jpg')
