from fastapi import Request, Response
from starlette.datastructures import MutableHeaders

# Basic CSP/HSTS and security headers (tweak as needed for your domain and CDN paths)
CSP = "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; connect-src *"

async def security_headers_middleware(request: Request, call_next):
    response: Response = await call_next(request)
    headers = MutableHeaders(response.headers)
    headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
    headers["Content-Security-Policy"] = CSP
    headers["X-Content-Type-Options"] = "nosniff"
    headers["X-Frame-Options"] = "DENY"
    headers["Referrer-Policy"] = "no-referrer"
    return response
