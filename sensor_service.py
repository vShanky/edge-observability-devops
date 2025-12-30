import time
import random
from flask import Flask, jsonify, Response
from prometheus_client import (
    Counter,
    Gauge,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST
)

app = Flask(__name__)

# Reduced from original large blob to avoid memory spikes
data_blob = "X" * 1_000_000  # ~1MB

# Prometheus metrics
REQUEST_COUNT = Counter(
    "sensor_requests_total",
    "Total number of requests to the sensor service"
)

CPU_SPIKE = Gauge(
    "sensor_cpu_spike",
    "Simulated CPU spike indicator"
)

PROCESS_LATENCY = Histogram(
    "sensor_processing_latency_seconds",
    "Time spent processing metrics request"
)

@app.route("/metrics")
def metrics():
    start = time.time()

    # Simulate small, predictable work instead of CPU-heavy loop
    time.sleep(0.01)  # 10ms

    PROCESS_LATENCY.observe(time.time() - start)
    CPU_SPIKE.set(random.randint(0, 1))
    REQUEST_COUNT.inc()

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/sensor")
def sensor():
    if random.random() < 0.2:
        return jsonify({"data": data_blob})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
