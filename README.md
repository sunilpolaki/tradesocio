##  Features

- FastAPI-based API
- Echoes request headers, method, and JSON body
- Dockerized for portability
- CI/CD with GitHub Actions
- Helm chart for Kubernetes deployment
- Ready for Prometheus instrumentation
- Clean, cloud-native structure (12-factor style)

#  TradeSocio FastAPI Demo

A demo project built with **FastAPI**, Docker, CI/CD via **GitHub Actions**, and deployed using **Kubernetes with Helm**. This solution demonstrates containerization, automation, and cloud-native deployment best practices.


##  API Test Case

**Endpoint:**

```bash
curl -X POST http://localhost:8000/api \
  -H "Content-Type: application/json" \
  -d '{"username":"xyz","password":"xyz"}'

Response
{
  "message": "Welcome to our demo API, here are the details of your request:",
  "headers": { ... },
  "method": "POST",
  "body": "{\"username\":\"xyz\",\"password\":\"xyz\"}"
}

---

 **Running Locally with Docker**
1. Build the Docker image:
docker build -t fastapi-app:latest .
2. Run the container:
docker run -d -p 8000:8000 fastapi-app
3. Test the endpoint:
Visit http://localhost:8000/docs or use curl as shown above.

 **CI/CD with GitHub Actions**
CI/CD is configured in .github/workflows/ci-cd.yml:
Runs on push to main
Installs dependencies & runs tests
Builds Docker image
Pushes to Docker Hub (set DOCKER_USERNAME and DOCKER_PASSWORD in secrets)

**Kubernetes with Helm**
1. Package and install via Helm:
cd helm/fastapi-app
helm install fastapi-app .
2. Port-forward to access the app:
kubectl port-forward svc/fastapi-app 8000:80
Visit: http://localhost:8000/docs

**Project Structure**
.
├── main.py               # FastAPI app
├── Dockerfile            # Docker build
├── requirements.txt
├── .github/workflows/    # GitHub Actions pipeline
└── helm/fastapi-app/     # Helm chart

 Prometheus Integration (Optional)
Instrument your FastAPI app using prometheus_client:
from prometheus_client import Counter
request_counter = Counter("api_requests_total", "Total number of requests")
@app.post("/api")
def handle(request: Request, body: dict):
    request_counter.inc()
    ...
TODOs / Future Improvements
Add unit/integration tests for CI

Add Helm test hook

Deploy to K3s or managed Kubernetes cluster

Add Open Policy Agent policies

Create GitHub deploy workflow with kubectl context

Submission
Public GitHub Repo: https://github.com/sunilpolaki/tradesocio

 Notes
This solution follows best practices:

12-Factor app principles

Docker layering & security

Kubernetes native deployment

Declarative configuration with Helm


Project Structure

.
├── main.py                     # FastAPI app
├── Dockerfile
├── requirements.txt
├── .github/workflows/
│   └── ci-cd.yml               # GitHub Actions CI/CD pipeline
└── helm/
    └── fastapi-app/          
