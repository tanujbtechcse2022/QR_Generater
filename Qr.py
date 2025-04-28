import qrcode

# Function to generate QR Code
def generate_qr(data, filename='myqrcode.png'):
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
        box_size=10,  # size of each box in the QR code
        border=4,  # thickness of the border
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code generated and saved as: {filename}")

# Example usage
generate_qr("https://www.yourwebsite.com", "your_qrcode.png")
