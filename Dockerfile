FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir flask prometheus_client gunicorn

# Single worker to keep memory predictable on low-resource systems
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "sensor_service:app"]
