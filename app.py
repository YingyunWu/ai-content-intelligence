import streamlit as st
import pandas as pd

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


# Analysis mode
st.sidebar.header("⚙️ Analysis Mode")

analysis_mode = st.sidebar.radio(
    "Choose an analysis mode:",
    [
        "Single Article",
        "Multi-Article Comparison"
    ]
)


# ============================================================
# Single Article Analysis
# ============================================================

if analysis_mode == "Single Article":

    st.subheader("📰 Single Article Analysis")

    article = st.text_area(
        "Paste your article below:",
        height=300,
        placeholder="Paste an article or news text here..."
    )

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


# ============================================================
# Multi-Article Comparison
# ============================================================

else:

    st.subheader("📊 Multi-Article Comparison")

    st.write(
        "Compare 2–10 articles to identify patterns and differences "
        "across sources."
    )


    # Number of articles
    num_articles = st.slider(
        "Number of articles",
        min_value=2,
        max_value=10,
        value=2
    )


    articles = []


    # Article input fields
    for i in range(num_articles):

        st.markdown(f"### Article {i + 1}")

        source = st.text_input(
            "Source",
            placeholder="e.g. Reuters, BBC, The Guardian",
            key=f"source_{i}"
        )

        date = st.date_input(
            "Publication Date",
            key=f"date_{i}"
        )

        article_text = st.text_area(
            "Article Text",
            height=200,
            placeholder="Paste article text here...",
            key=f"article_{i}"
        )

        articles.append(
            {
                "source": source,
                "date": date,
                "article": article_text
            }
        )


    # Analyze button
    if st.button("🔍 Analyze Articles"):

        # Check whether all articles have content
        incomplete = False

        for article in articles:

            if not article["article"].strip():
                incomplete = True
                break


        if incomplete:

            st.warning(
                "Please enter text for all articles before analyzing."
            )

        else:

            results = []

            progress = st.progress(0)

            with st.spinner("Analyzing articles..."):

                for i, article in enumerate(articles):

                    try:

                        result = analyze_article(
                            article["article"]
                        )

                        results.append(
                            {
                                "Source": article["source"],
                                "Date": article["date"],
                                "Topic": result["topic"],
                                "Sentiment": result["sentiment"],
                                "Primary Keywords": ", ".join(
                                    result["primary_keywords"]
                                )
                            }
                        )

                    except Exception as e:

                        st.error(
                            f"Analysis failed for Article {i + 1}: {e}"
                        )

                        st.stop()


                    progress.progress(
                        (i + 1) / len(articles)
                    )


            # Create comparison dataset
            df = pd.DataFrame(results)


            st.subheader("📊 Article Comparison")

            st.dataframe(
                df,
                use_container_width=True
            )