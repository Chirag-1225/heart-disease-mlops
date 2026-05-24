# Use an official lightweight Python runtime
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirement files first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else into the container
COPY . .

# Run the training script during image build to generate the model artifacts
RUN python src/train.py

# Expose the Flask API port
EXPOSE 5000

# Define command to run the web application
CMD ["python", "src/app.py"]