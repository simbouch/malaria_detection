# Use a lightweight Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install necessary system dependencies and clean up
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to optimize Docker caching
COPY requirements.txt /app/

# Install Python dependencies without cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the application port
EXPOSE 80

# Start the application using Gunicorn with optimized settings
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "2", "--threads", "4", "app:app"]
