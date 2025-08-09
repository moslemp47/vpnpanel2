from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
from .config import get_settings
from .routers import v1, v2, auth, admin, payments, tickets, mobile
from .security import security_headers_middleware

app = FastAPI(title="CloudVPS Pro API", version="3.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security headers (HSTS, CSP, etc.)
app.middleware("http")(security_headers_middleware)

# Prometheus metrics
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint", "status"])
LATENCY = Histogram("http_request_duration_seconds", "Request latency", ["endpoint"])

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    with LATENCY.labels(endpoint=request.url.path).time():
        response: Response = await call_next(request)
    REQUESTS.labels(method=request.method, endpoint=request.url.path, status=response.status_code).inc()
    return response

@app.get("/healthz", tags=["health"])
async def healthz():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Routers
app.include_router(v1.router, prefix="/api/v1")
app.include_router(v2.router, prefix="/api/v2")
app.include_router(auth.router, prefix="/api")
app.include_router(admin.router, prefix="/api/admin")
app.include_router(payments.router, prefix="/api/payments")
app.include_router(tickets.router, prefix="/api")
app.include_router(mobile.router, prefix="/api/mobile")
