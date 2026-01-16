# app/services/openai_client.py

from app.config import settings
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
