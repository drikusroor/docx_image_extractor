# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create folders for uploads and extracted images
RUN mkdir -p /app/uploads /app/extracted

# Use a non-root user for security
RUN useradd -m appuser
USER appuser

# Expose port
EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]
