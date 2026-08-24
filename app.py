import os
import json

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


# Load API key from .env
load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    st.error("DEEPSEEK_API_KEY is not configured.")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


# Page configuration
st.set_page_config(
    page_title="AI Content Intelligence",
    page_icon="📰",
    layout="wide"
)


# Header
st.title("📰 AI Content Intelligence Platform")

st.write(
    "An LLM-powered platform for content intelligence "
    "and computational media analysis."
)


# Article input
st.subheader("Article Analysis")

article = st.text_area(
    "Paste your article below:",
    height=300,
    placeholder="Paste an article or news text here..."
)


# Analyze button
if st.button("🔍 Analyze Article"):

    if not article.strip():
        st.warning("Please enter an article first.")

    else:

        with st.spinner("Analyzing article..."):

            prompt = f"""
You are an AI content analysis assistant.

Analyze the following article and return a JSON object with exactly
these fields:

- summary
- key_points
- topic
- sentiment

Rules:

summary:
Provide a concise summary of the article.

key_points:
Provide 3 to 5 important points.

topic:
Identify the primary topic of the article.

sentiment:
Classify the overall sentiment as Positive, Neutral, or Negative.

Article:

{article}
"""

            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a precise content analysis assistant."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format={"type": "json_object"}
            )

            result = json.loads(
                response.choices[0].message.content
            )


        # Display results
        st.subheader("📄 Summary")
        st.write(result["summary"])


        st.subheader("🔑 Key Points")

        for point in result["key_points"]:
            st.write(f"- {point}")


        st.subheader("🏷️ Topic")
        st.write(result["topic"])


        st.subheader("💭 Sentiment")
        st.write(result["sentiment"])