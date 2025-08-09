from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from pydantic import BaseModel, EmailStr
import pyotp, time

router = APIRouter(tags=["auth"])

class Login(BaseModel):
    email: EmailStr
    password: str
    captcha_token: str | None = None

@router.post("/login")
async def login(payload: Login):
    # TODO: verify captcha, password, create JWT, track session+device
    return {"access": "jwt_access_token", "refresh": "jwt_refresh_token"}

class Register(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
async def register(payload: Register):
    # TODO: create user, send verification email
    return {"ok": True}

@router.post("/2fa/setup")
async def twofa_setup():
    # In reality, store secret and return provisioning URI/QR
    secret = pyotp.random_base32()
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name="user@example.com", issuer_name="CloudVPS Pro")
    return {"secret": secret, "otpauth": uri}

class TwoFAVerify(BaseModel):
    token: str
    secret: str

@router.post("/2fa/verify")
async def twofa_verify(body: TwoFAVerify):
    totp = pyotp.TOTP(body.secret)
    if totp.verify(body.token, valid_window=1):
        return {"verified": True}
    raise HTTPException(400, "Invalid token")

@router.post("/avatar")
async def upload_avatar(file: UploadFile = File(...)):
    # TODO: save to S3/local
    return {"filename": file.filename}
