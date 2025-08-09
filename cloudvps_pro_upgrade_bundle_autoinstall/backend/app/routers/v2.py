from fastapi import APIRouter

router = APIRouter(tags=["v2"])

@router.get("/status")
async def status():
    return {"api": "v2", "ok": True, "new": True}
