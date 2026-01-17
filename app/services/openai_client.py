from openai import OpenAI
import os

# Create OpenAI client ONCE
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(system_prompt, user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        # This prevents UI from breaking
        print("OpenAI Error:", e)
        return "⚠️ AI service is temporarily unavailable. Please try again."
