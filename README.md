# Lightweight Observability Stack for Resource-Constrained Systems

This project demonstrates how I deployed and debugged a Python sensor service with a lightweight observability stack (Prometheus + Grafana) under strict memory and CPU constraints.

The focus of this work was not on rewriting application logic, but on identifying performance bottlenecks, fixing Prometheus scrape failures, and keeping the entire system stable under limited resources — similar to edge or robotics environments.

---

## Problem Statement

The provided Python service had intentional inefficiencies which caused:

- CPU spikes during `/metrics` scraping
- Memory jumps due to large in-memory payloads
- Prometheus scrape failures
- Unstable observability behavior on low-resource systems

---

## What I Changed (Minimal & Debug-Focused)

I intentionally kept code changes minimal and focused only on DevOps-level debugging:

- Reduced CPU-heavy logic inside the `/metrics` endpoint
- Fixed Prometheus scrape failures by returning the correct content-type
- Reduced memory usage by limiting large in-memory objects
- Added container-level memory limits
- Tuned Prometheus scrape interval and retention
- Used Gunicorn instead of Flask’s dev server for stability

No core application logic was rewritten.

---

## Observability Stack

- **Prometheus**
  - 10s scrape interval
  - 1h retention
  - WAL compression enabled

- **Grafana**
  - Lightweight default setup
  - No extra plugins installed
  - Memory capped via Docker

---

## Architecture Overview

```
Client
  |
  v
Python Sensor Service (Docker)
  |
  v
Prometheus
  |
  v
Grafana
```

---

## Resource Usage Summary

| Component        | Memory Usage |
|------------------|-------------|
| Sensor Service   | ~50 MB      |
| Prometheus       | ~25 MB      |
| Grafana          | ~70–80 MB   |
| **Total**        | **~150 MB** |

The full stack runs comfortably under the 300 MB limit.

---

## How to Run

```bash
docker compose build --no-cache
docker compose up
```

### Access:
- Sensor API: http://localhost:8000/sensor
- Metrics: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

---

## What I’d Improve With More Time

- Add alerting for scrape failures
- Evaluate VictoriaMetrics for lower memory usage
- Add a simple CI pipeline for build validation

---

### Note

This project reflects my own implementation and debugging work.  
AI tools were used only for learning and validating concepts, not for generating the solution end-to-end.
