import os
import qrcode

# Your GitHub URL
github_url = "https://github.com/yourusername"

# Create output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Save the QR code in the output folder
output_path = os.path.join(output_dir, "github_qr.png")
qr = qrcode.make(github_url)
qr.save(output_path)

print(f"✅ QR code saved at: {output_path}")
