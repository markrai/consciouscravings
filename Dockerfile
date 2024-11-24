# Use an official Python image as the base
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering outputs
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Flask app
EXPOSE 8000

# Run the Flask application
CMD ["python", "app.py"]
