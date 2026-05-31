import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Step 1: Take input from user
data = input("Enter text or URL to generate QR Code: ")

# Step 2 & 3: Encode data and add error correction
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,  # High error correction (~30%)
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Step 4: Create and save QR image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print("QR Code generated successfully!")
print("Saved as 'qrcode.png'")