from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()
REQUEST_COUNT = Counter('api_requests_total', 'Total number of API requests')

@app.get("/api")
@app.post("/api")
async def root(request: Request):
    REQUEST_COUNT.inc()
    headers = dict(request.headers)
    body = await request.body()
    return {
        "message": "Welcome to our demo API, here are the details of your request:",
        "headers": headers,
        "method": request.method,
        "body": body.decode("utf-8") if body else None,
    }

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type="text/plain")

