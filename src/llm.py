import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def get_client():
    api_key = os.getenv("DEEPSEEK_API_KEY")

    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY is not configured.")

    return OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )


def analyze_article(article: str) -> dict:
    client = get_client()

    system_prompt = """
You are an AI content analysis assistant.

Analyze the article provided by the user.

Return a JSON object with exactly these fields:

summary:
A concise summary of the article.

key_points:
A list containing 3 to 5 important points.

topic:
The primary topic of the article.

sentiment:
The overall sentiment. Use only:
Positive, Neutral, or Negative.
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": article
            }
        ],
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("The model returned an empty response.")

    return json.loads(content)