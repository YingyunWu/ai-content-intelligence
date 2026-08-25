import streamlit as st

from src.llm import analyze_article


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

            try:
                result = analyze_article(article)

            except Exception as e:
                st.error(f"Analysis failed: {e}")
                st.stop()


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

        st.subheader("🎯 Target Audience")
        st.write(result["target_audience"])

        st.subheader("💡 Audience Needs")

        for need in result["audience_needs"]:
            st.write(f"- {need}")

        st.subheader("🔎 Primary Keywords")
        st.write(", ".join(result["primary_keywords"]))

        st.subheader("🔗 Secondary Keywords")
        st.write(", ".join(result["secondary_keywords"]))

        st.subheader("🎯 Search Intent")
        st.write(result["search_intent"])
