# Use an official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy Python script to the container
COPY qr_generator.py .
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "qr_generator.py"]
