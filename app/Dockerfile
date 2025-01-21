FROM python:3.10-slim

WORKDIR /app

# Add Python path to ensure the `app` module is recognized
ENV PYTHONPATH=/app

# Copy dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app

# Expose Flask port
EXPOSE 5000

WORKDIR /
# Run Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app"]
