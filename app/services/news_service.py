import json
from app.core.personas import NEWS_SYSTEM_PROMPT
from app.services.openai_client import generate_response

def news_reply(message: str):
    with open("app/data/mock_news.json") as f:
        news_data = json.load(f)

    prompt = f"""
    Based on the following news, summarize market conditions:

    {news_data}
    """

    return generate_response(NEWS_SYSTEM_PROMPT, prompt)
