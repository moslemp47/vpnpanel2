from fastapi import APIRouter

router = APIRouter(tags=["mobile"])

@router.get("/bootstrap")
async def bootstrap():
    return {
        "push_enabled": True,
        "biometric_supported": True,
        "auto_connect": True,
    }
