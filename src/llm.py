import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from src.prompts import CONTENT_ANALYSIS_SYSTEM_PROMPT


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

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": CONTENT_ANALYSIS_SYSTEM_PROMPT
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
