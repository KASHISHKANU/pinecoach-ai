# app/telegram_bot/bot.py

import requests
from fastapi import APIRouter, Request
from app.config import settings

router = APIRouter()

TELEGRAM_API = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}"

def send_message(chat_id: int, text: str):
    requests.post(
        f"{TELEGRAM_API}/sendMessage",
        json={"chat_id": chat_id, "text": text},
        timeout=10
    )

@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()

    if "message" not in data or "text" not in data["message"]:
        return {"ok": True}

    chat_id = data["message"]["chat"]["id"]
    user_text = data["message"]["text"]

    response = requests.post(
        f"{settings.BACKEND_URL}/chat",
        json={"message": user_text},
        timeout=10
    ).json()

    send_message(chat_id, response["response"])

    return {"ok": True}
