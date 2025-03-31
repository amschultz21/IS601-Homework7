# Use an official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy Python script to the container
COPY qr_generator.py .

# Install required Python packages
RUN pip install qrcode[pil]

# Run the script
CMD ["python", "qr_generator.py"]
