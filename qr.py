import qrcode

image = qrcode.make('http://124.0.0.1:8000')
image.save("qr.png")
