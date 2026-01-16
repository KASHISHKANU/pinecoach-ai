# app/core/orchestrator.py

from app.core.intent_detector import detect_intent
from app.core.safety import is_advice_request, refusal_response
from app.services.coach_service import coach_reply
from app.services.news_service import news_reply

def handle_message(user_message: str):
    if is_advice_request(user_message):
        return refusal_response()

    intent = detect_intent(user_message)

    if intent == "EDUCATION":
        return coach_reply(user_message)

    if intent == "MARKET_NEWS":
        return news_reply(user_message)

    return (
        "I can help you learn investing concepts or explain today’s market news.\n\n"
        "Try asking:\n"
        "- 'What is SIP?'\n"
        "- 'Why is the market down today?'"
    )
