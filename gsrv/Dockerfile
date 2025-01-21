FROM python:3.10-slim

WORKDIR /app

# Copy dependency requirements
COPY ../requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app into the container
COPY . .

# Copy the .env file into the container
COPY ../.env /app/.env

# Expose Flask port
EXPOSE 5000

# Run the Flask app with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "gsrv:create_app()"]
