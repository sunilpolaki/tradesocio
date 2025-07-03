## 📌 Features

- FastAPI-based API
- Echoes request headers, method, and JSON body
- Dockerized for portability
- CI/CD with GitHub Actions
- Helm chart for Kubernetes deployment
- Ready for Prometheus instrumentation
- Clean, cloud-native structure (12-factor style)

---

## 🧪 API Test Case

**Endpoint:**

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
🐳 Running Locally with Docker
1. Build the Docker image:
bash
Copy
Edit
docker build -t fastapi-app:latest .
2. Run the container:
bash
Copy
Edit
docker run -d -p 8000:8000 fastapi-app
3. Test the endpoint:
Visit http://localhost:8000/docs or use curl as shown above.

🔁 CI/CD with GitHub Actions
CI/CD is configured in .github/workflows/ci-cd.yml:

Runs on push to main

Installs dependencies & runs tests

Builds Docker image

Pushes to Docker Hub (set DOCKER_USERNAME and DOCKER_PASSWORD in secrets)

☸️ Kubernetes with Helm
1. Package and install via Helm:
bash
Copy
Edit
cd helm/fastapi-app
helm install fastapi-app .
2. Port-forward to access the app:
bash
Copy
Edit
kubectl port-forward svc/fastapi-app 8000:80
Visit: http://localhost:8000/docs

📂 Project Structure
bash
Copy
Edit
.
├── main.py               # FastAPI app
├── Dockerfile            # Docker build
├── requirements.txt
├── .github/workflows/    # GitHub Actions pipeline
└── helm/fastapi-app/     # Helm chart
📈 Prometheus Integration (Optional)
Instrument your FastAPI app using prometheus_client:

python
Copy
Edit
from prometheus_client import Counter

request_counter = Counter("api_requests_total", "Total number of requests")

@app.post("/api")
def handle(request: Request, body: dict):
    request_counter.inc()
    ...
✅ TODOs / Future Improvements
Add unit/integration tests for CI

Add Helm test hook

Deploy to K3s or managed Kubernetes cluster

Add Open Policy Agent policies

Create GitHub deploy workflow with kubectl context

📬 Submission
Public GitHub Repo: https://github.com/<your-username>/ts-devops-challenge

🧠 Notes
This solution follows best practices:

12-Factor app principles

Docker layering & security

Kubernetes native deployment

Declarative configuration with Helm

📜 License
MIT © 2025

yaml
Copy
Edit

---

Let me know if you'd like me to:
- Fill in the repo link
- Add specific examples of `main.py` code
- Include screenshots or Swagger output

Would you like a `README.md` file created and added to your repo locally?







You said:
need template to paste in github


ChatGPT said:
Here is a clean and professional GitHub-friendly README.md template for your TS DevOps Challenge project. You can copy-paste this directly into your repo:

markdown
Copy
Edit
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
🐳 Docker Instructions
Build the image:
bash
Copy
Edit
docker build -t fastapi-app:latest .
Run the container:
bash
Copy
Edit
docker run -d -p 8000:8000 fastapi-app
Test locally:
Open in browser: http://localhost:8000/docs
Or use curl as shown above.

🔁 CI/CD Pipeline (GitHub Actions)
CI/CD is automated via GitHub Actions (.github/workflows/ci-cd.yml):

Triggered on push to main

Installs dependencies

Runs tests

Builds and pushes Docker image to Docker Hub

Set these repository secrets:

DOCKER_USERNAME

DOCKER_PASSWORD

☸️ Kubernetes Deployment via Helm
1. Install using Helm:
bash
Copy
Edit
cd helm/fastapi-app
helm install fastapi-app .
2. Port-forward service:
bash
Copy
Edit
kubectl port-forward svc/fastapi-app 8000:80
Access app at http://localhost:8000/docs

📁 Project Structure
bash
Copy
Edit
.
├── main.py                     # FastAPI app
├── Dockerfile
├── requirements.txt
├── .github/workflows/
│   └── ci-cd.yml               # GitHub Actions CI/CD pipeline
└── helm/
    └── fastapi-app/            # Helm chart for deployment
🧩 Optional: Prometheus Metrics
Add Prometheus instrumentation with prometheus_client:

python
Copy
Edit
from prometheus_client import Counter

request_counter = Counter("api_requests_total", "Total number of requests")
Metrics can be exposed at /metrics for scraping.

✅ TODOs
 Add tests with pytest

 Add Helm test hook

 Add OPA policy validation (non-root user, no default SA)

 GitHub deploy workflow with kubectl

📬 Submission
Please visit the public repo:
👉 https://github.com/your-username/ts-devops-challenge

🧠 Notes
This project follows DevOps best practices:

12-factor app structure

Cloud-native design

Declarative infrastructure

GitOps-compatible CI/CD

📜 License
MIT © 2025

yaml
Copy
Edit

---

### 🛠️ Final Steps:
- Replace `your-username` with your actual GitHub username.
- Add this file to your repo as `README.md` and commit it:

```bash
git add README.md
git commit -m "Add README documentation"
git push origin main
