from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/stats")
async def stats():
    return {
        "users": 1234,
        "active_subscriptions": 456,
        "mrr": 7890,
    }
