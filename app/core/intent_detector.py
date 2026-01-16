def detect_intent(message: str) -> str:
    msg = message.lower()

    if any(x in msg for x in ["why market", "market today", "news", "sensex", "nifty"]):
        return "MARKET_NEWS"

    if any(x in msg for x in ["what is", "explain", "how does", "difference"]):
        return "EDUCATION"

    return "UNKNOWN"
