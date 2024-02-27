import qrcode

# Data to be encoded
data = "https://www.example.com"

# Creating an instance of QRCode class
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adding data to the instance
qr.add_data(data)
qr.make(fit=True)

# Creating an Image object from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Saving the image
img.save("example_qr.png")
