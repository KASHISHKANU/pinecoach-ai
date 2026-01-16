from app.core.personas import COACH_SYSTEM_PROMPT
from app.services.openai_client import generate_response

def coach_reply(message: str):
    return generate_response(COACH_SYSTEM_PROMPT, message)
