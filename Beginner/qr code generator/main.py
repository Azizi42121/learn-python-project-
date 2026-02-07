import qrcode

url = input("Enter the URL: ").strip()
file_path = "D:\\project (learning) python\\Beginner\\qr code generator\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)