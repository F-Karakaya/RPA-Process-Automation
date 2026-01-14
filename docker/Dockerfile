# Base Image with Python 3.9
FROM python:3.9-slim

# Set Working Directory
WORKDIR /app

# Install System Dependencies (Tesseract OCR, etc.)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy Requirements
COPY requirements.txt .

# Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download Spacy Model
RUN python -m spacy download en_core_web_sm

# Copy Application Code
COPY . .

# Expose API Port
EXPOSE 8000

# Set Environment Variables
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production

# Entrypoint: Run AI Service API (Simulated with Uvicorn if we had api.py, or just shell)
# For this repo, we keep it ready for command execution
CMD ["python", "orchestration/job_scheduler.py"]
