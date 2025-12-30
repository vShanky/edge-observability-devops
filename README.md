# Lightweight Observability Stack for Resource-Constrained Systems

This project demonstrates how I debugged and deployed a Python service with a lightweight observability stack (Prometheus + Grafana) under strict resource limits.

The focus was not on rewriting application logic, but on identifying performance bottlenecks, fixing scrape failures, and keeping the entire stack below a 300 MB memory budget — similar to edge or robotics environments.

