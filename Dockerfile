# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8001 for the Flask app
EXPOSE 8001

# Run the Flask app
CMD ["python", "calc.py"]
