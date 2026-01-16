BANNED_KEYWORDS = [
    "buy", "sell", "intraday", "tips",
    "best stock", "guaranteed", "returns",
    "portfolio", "recommend", "suggest"
]

DISCLAIMER = "⚠️ Educational purposes only. This is not financial advice."

def is_advice_request(user_message: str) -> bool:
    msg = user_message.lower()
    return any(keyword in msg for keyword in BANNED_KEYWORDS)

def refusal_response():
    return (
        "I can’t help with stock recommendations or trading tips.\n\n"
        "However, I *can* teach you **how investors evaluate stocks**, "
        "understand risk, or explain market concepts.\n\n"
        f"{DISCLAIMER}"
    )
