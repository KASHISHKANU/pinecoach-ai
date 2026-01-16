from fastapi import APIRouter
from pydantic import BaseModel
from app.core.orchestrator import handle_message

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    reply = handle_message(payload.message)
    return {"response": reply}
