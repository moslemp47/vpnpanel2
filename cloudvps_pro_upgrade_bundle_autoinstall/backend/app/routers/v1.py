from fastapi import APIRouter

router = APIRouter(tags=["v1"])

@router.get("/status")
async def status():
    return {"api": "v1", "ok": True}
