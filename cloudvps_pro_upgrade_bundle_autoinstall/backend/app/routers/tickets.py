from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["tickets"])

class Ticket(BaseModel):
    subject: str
    message: str
    priority: str = "Low"
    department: str = "Support"

@router.post("/tickets")
async def create_ticket(t: Ticket):
    # TODO: persist, notify, SLA timers
    return {"id": 1, **t.model_dump()}
