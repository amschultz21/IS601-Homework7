import qrcode

# Replace with your actual GitHub URL
github_url = "https://github.com/amschultz21"

# Generate QR Code
qr = qrcode.make(github_url)

# Save the QR Code to a file
qr.save("github_qr.png")

print("QR code generated and saved as github_qr.png!")
