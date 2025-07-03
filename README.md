# tradesocio

# 🚀 TS DevOps Challenge – FastAPI Microservice

This repository contains a simple FastAPI application that echoes request headers, method, and body. It is fully containerized, integrated with GitHub Actions for CI/CD, and deployable to Kubernetes via Helm.

---

## 📦 Features

- ✅ FastAPI microservice
- ✅ POST `/api` endpoint: echoes request headers, method, and body
- ✅ Dockerized application
- ✅ CI/CD with GitHub Actions
- ✅ Helm chart for Kubernetes deployment
- ✅ Swagger UI at `/docs`
- ✅ Prometheus-ready instrumentation (optional)

---

## 🧪 Example Request

```bash
curl -X POST http://localhost:8000/api \
  -H "Content-Type: application/json" \
  -d '{"username":"xyz","password":"xyz"}'
Response:

json
Copy
Edit
{
  "message": "Welcome to our demo API, here are the details of your request:",
  "headers": { ... },
  "method": "POST",
  "body": "{\"username\":\"xyz\",\"password\":\"xyz\"}"
}
