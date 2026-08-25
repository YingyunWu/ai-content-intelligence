import streamlit as st
import pandas as pd

from src.llm import analyze_article
from src.semantic import (
    group_similar_topics,
    get_representative_topic
)


# ============================================================
# Demo Data
# ============================================================

DEMO_RESULTS = [
    {
        "Topic": "Marriage and changing social attitudes",
        "Sentiment": "Neutral",
        "Search Intent": "Informational",
        "Primary Frame": "Social Impact",
        "Generic Frames": "Human Interest",
        "Issue-Specific Frames": "Social Impact",
        "Primary Keywords": "marriage, young adults, social attitudes"
    },
    {
        "Topic": "Economic pressures and marriage decisions",
        "Sentiment": "Negative",
        "Search Intent": "Informational",
        "Primary Frame": "Economic Consequences",
        "Generic Frames": "Economic Consequences",
        "Issue-Specific Frames": "Social Impact, Risk & Threat",
        "Primary Keywords": "marriage, housing costs, financial pressure"
    },
    {
        "Topic": "Marriage policy and demographic change",
        "Sentiment": "Neutral",
        "Search Intent": "Informational",
        "Primary Frame": "Policy & Regulation",
        "Generic Frames": "Responsibility",
        "Issue-Specific Frames": "Policy & Regulation, Social Impact",
        "Primary Keywords": "marriage policy, demographics, population"
    },
    {
        "Topic": "Technology and changing relationships",
        "Sentiment": "Positive",
        "Search Intent": "Informational",
        "Primary Frame": "Technology & Innovation",
        "Generic Frames": "Human Interest",
        "Issue-Specific Frames": "Technology & Innovation",
        "Primary Keywords": "technology, relationships, dating"
    },
    {
        "Topic": "Risks associated with changing family structures",
        "Sentiment": "Negative",
        "Search Intent": "Informational",
        "Primary Frame": "Risk & Threat",
        "Generic Frames": "Risk & Threat",
        "Issue-Specific Frames": "Risk & Threat, Social Impact",
        "Primary Keywords": "family structure, social risk, marriage"
    },
    {
        "Topic": "Individual choice and marriage",
        "Sentiment": "Positive",
        "Search Intent": "Informational",
        "Primary Frame": "Human Interest",
        "Generic Frames": "Human Interest, Morality",
        "Issue-Specific Frames": "Social Impact",
        "Primary Keywords": "individual choice, marriage, personal values"
    },
    {
        "Topic": "Marriage expectations among young people",
        "Sentiment": "Neutral",
        "Search Intent": "Informational",
        "Primary Frame": "Human Interest",
        "Generic Frames": "Human Interest",
        "Issue-Specific Frames": "Social Impact",
        "Primary Keywords": "young people, marriage expectations"
    },
    {
        "Topic": "Government responses to demographic challenges",
        "Sentiment": "Neutral",
        "Search Intent": "Informational",
        "Primary Frame": "Policy & Regulation",
        "Generic Frames": "Responsibility",
        "Issue-Specific Frames": "Policy & Regulation",
        "Primary Keywords": "government policy, demographics, marriage"
    },
    {
        "Topic": "The economic impact of declining marriage rates",
        "Sentiment": "Negative",
        "Search Intent": "Informational",
        "Primary Frame": "Economic Consequences",
        "Generic Frames": "Economic Consequences",
        "Issue-Specific Frames": "Social Impact",
        "Primary Keywords": "marriage rates, economy, demographics"
    },
    {
        "Topic": "Changing cultural perceptions of marriage",
        "Sentiment": "Neutral",
        "Search Intent": "Informational",
        "Primary Frame": "Morality",
        "Generic Frames": "Morality, Human Interest",
        "Issue-Specific Frames": "Social Impact",
        "Primary Keywords": "marriage, culture, values"
    }
]


# ============================================================
# Helper Functions
# ============================================================

def get_demo_result(index):
    """Return a simulated analysis result."""
    return DEMO_RESULTS[index % len(DEMO_RESULTS)]


def analyze_content(content, api_mode):
    """Analyze content using Demo or Live API mode."""

    if api_mode == "Demo / Mock Data":
        return get_demo_result(0)

    return analyze_article(content)


def analyze_multiple_contents(contents, api_mode):
    """Analyze multiple content items."""

    results = []

    progress = st.progress(0)

    with st.spinner("Analyzing content..."):

        for i, content in enumerate(contents):

            try:

                if api_mode == "Demo / Mock Data":

                    result = get_demo_result(i)

                    results.append(
                        {
                            "Source": content["source"],
                            "Content Type": content["content_type"],
                            "Date": content["date"],
                            "Topic": result["Topic"],
                            "Sentiment": result["Sentiment"],
                            "Search Intent": result["Search Intent"],
                            "Primary Frame": result["Primary Frame"],
                            "Generic Frames": result["Generic Frames"],
                            "Issue-Specific Frames": result[
                                "Issue-Specific Frames"
                            ],
                            "Primary Keywords": result[
                                "Primary Keywords"
                            ]
                        }
                    )

                else:

                    result = analyze_article(
                        content["text"]
                    )

                    results.append(
                        {
                            "Source": content["source"],
                            "Content Type": content["content_type"],
                            "Date": content["date"],
                            "Topic": result["topic"],
                            "Sentiment": result["sentiment"],
                            "Search Intent": result["search_intent"],
                            "Primary Frame": result["primary_frame"],
                            "Generic Frames": ", ".join(
                                result["generic_frames"]
                            ),
                            "Issue-Specific Frames": ", ".join(
                                result["issue_specific_frames"]
                            ),
                            "Primary Keywords": ", ".join(
                                result["primary_keywords"]
                            )
                        }
                    )

            except Exception as e:

                st.error(
                    f"Analysis failed for Content {i + 1}: {e}"
                )

                st.stop()

            progress.progress(
                (i + 1) / len(contents)
            )

    return results


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="AI Content Intelligence",
    page_icon="📰",
    layout="wide"
)


# ============================================================
# Header
# ============================================================

st.title("📰 AI Content Intelligence Platform")

st.write(
    "An LLM-powered platform for content intelligence "
    "and computational media analysis."
)


# ============================================================
# Sidebar
# ============================================================

st.sidebar.header("⚙️ Analysis Mode")

analysis_mode = st.sidebar.radio(
    "Choose an analysis mode:",
    [
        "Single Content",
        "Multi-Content Comparison"
    ]
)


st.sidebar.header("🔧 API Mode")

api_mode = st.sidebar.radio(
    "Choose how to run the analysis:",
    [
        "Demo / Mock Data",
        "Live API"
    ]
)


if api_mode == "Demo / Mock Data":

    st.sidebar.info(
        "Demo mode uses simulated results. "
        "No API calls are made."
    )

else:

    st.sidebar.warning(
        "Live API mode uses your DeepSeek API "
        "and may consume credits."
    )


# ============================================================
# Content Type Options
# ============================================================

CONTENT_TYPES = [
    "News Article",
    "Social Media Post",
    "Comment",
    "Forum Post",
    "Other"
]


# ============================================================
# Single Content Analysis
# ============================================================

if analysis_mode == "Single Content":

    st.subheader("📰 Single Content Analysis")

    st.write(
        "Analyze a news article, social media post, comment, "
        "or other user-generated content."
    )


    # ------------------------------------------------
    # Content Metadata
    # ------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        content_type = st.selectbox(
            "Content Type",
            CONTENT_TYPES
        )


    with col2:

        source = st.text_input(
            "Source / Platform",
            placeholder="e.g. BBC, Xiaohongshu, Reddit, X"
        )


    # ------------------------------------------------
    # Content Input
    # ------------------------------------------------

    content = st.text_area(
        "Content",
        height=300,
        placeholder="Paste your content here..."
    )


    if st.button("🔍 Analyze Content"):

        if not content.strip():

            st.warning(
                "Please enter some content first."
            )

        else:

            with st.spinner("Analyzing content..."):

                try:

                    if api_mode == "Demo / Mock Data":

                        result = get_demo_result(0)

                    else:

                        result = analyze_article(
                            content
                        )

                except Exception as e:

                    st.error(
                        f"Analysis failed: {e}"
                    )

                    st.stop()


            # ------------------------------------------------
            # Basic Content Analysis
            # ------------------------------------------------

            st.subheader("📄 Summary")

            if api_mode == "Demo / Mock Data":

                st.write(
                    "This is a demonstration of how the platform "
                    "can analyze different types of content."
                )

            else:

                st.write(
                    result["summary"]
                )


            st.subheader("🔑 Key Points")

            if api_mode == "Demo / Mock Data":

                st.write(
                    "- Identifies the main ideas and themes."
                )

                st.write(
                    "- Extracts important information from the content."
                )

                st.write(
                    "- Produces structured content intelligence."
                )

            else:

                for point in result["key_points"]:

                    st.write(
                        f"- {point}"
                    )


            st.subheader("🏷️ Topic")

            if api_mode == "Demo / Mock Data":

                st.write(
                    result["Topic"]
                )

            else:

                st.write(
                    result["topic"]
                )


            st.subheader("💭 Sentiment")

            if api_mode == "Demo / Mock Data":

                st.write(
                    result["Sentiment"]
                )

            else:

                st.write(
                    result["sentiment"]
                )


            # ------------------------------------------------
            # Audience Analysis
            # ------------------------------------------------

            st.subheader("🎯 Target Audience")

            if api_mode == "Demo / Mock Data":

                st.write(
                    "People interested in social trends, "
                    "public discourse, and changing attitudes."
                )

            else:

                st.write(
                    result["target_audience"]
                )


            st.subheader("💡 Audience Needs")

            if api_mode == "Demo / Mock Data":

                st.write(
                    "- Understand the main issue."
                )

                st.write(
                    "- Understand the social context."
                )

                st.write(
                    "- Identify relevant trends and perspectives."
                )

            else:

                for need in result["audience_needs"]:

                    st.write(
                        f"- {need}"
                    )


            # ------------------------------------------------
            # SEO Analysis
            # ------------------------------------------------

            st.subheader("🔎 Primary Keywords")

            if api_mode == "Demo / Mock Data":

                st.write(
                    "marriage, young adults, social attitudes"
                )

            else:

                st.write(
                    ", ".join(
                        result["primary_keywords"]
                    )
                )


            st.subheader("🔗 Secondary Keywords")

            if api_mode == "Demo / Mock Data":

                st.write(
                    "relationships, society, demographic change"
                )

            else:

                st.write(
                    ", ".join(
                        result["secondary_keywords"]
                    )
                )


            st.subheader("🔍 Search Intent")

            if api_mode == "Demo / Mock Data":

                st.write(
                    result["Search Intent"]
                )

            else:

                st.write(
                    result["search_intent"]
                )


            # ------------------------------------------------
            # Framing Analysis
            # ------------------------------------------------

            st.subheader("🧩 Content Framing")


            st.markdown(
                "**Primary Frame**"
            )

            if api_mode == "Demo / Mock Data":

                st.write(
                    result["Primary Frame"]
                )

            else:

                st.write(
                    result["primary_frame"]
                )


            st.markdown(
                "**Generic News Frames**"
            )

            if api_mode == "Demo / Mock Data":

                st.write(
                    f"- {result['Generic Frames']}"
                )

            elif result["generic_frames"]:

                for frame in result["generic_frames"]:

                    st.write(
                        f"- {frame}"
                    )

            else:

                st.write(
                    "No clear generic frame identified."
                )


            st.markdown(
                "**Issue-Specific Frames**"
            )

            if api_mode == "Demo / Mock Data":

                st.write(
                    f"- {result['Issue-Specific Frames']}"
                )

            elif result["issue_specific_frames"]:

                for frame in result["issue_specific_frames"]:

                    st.write(
                        f"- {frame}"
                    )

            else:

                st.write(
                    "No clear issue-specific frame identified."
                )


# ============================================================
# Multi-Content Comparison
# ============================================================

else:

    st.subheader("📊 Multi-Content Comparison")

    st.write(
        "Compare 2–10 pieces of content across news media, "
        "social media, comments, and other sources."
    )


    # ------------------------------------------------
    # Number of Contents
    # ------------------------------------------------

    num_contents = st.slider(
        "Number of contents",
        min_value=2,
        max_value=10,
        value=2
    )


    contents = []


    # ------------------------------------------------
    # Content Input
    # ------------------------------------------------

    for i in range(num_contents):

        st.markdown(
            f"### Content {i + 1}"
        )


        col1, col2 = st.columns(2)


        with col1:

            content_type = st.selectbox(
                "Content Type",
                CONTENT_TYPES,
                key=f"content_type_{i}"
            )


        with col2:

            source = st.text_input(
                "Source / Platform",
                placeholder="e.g. BBC, Xiaohongshu, Reddit",
                key=f"source_{i}"
            )


        date = st.date_input(
            "Publication Date",
            key=f"date_{i}"
        )


        content_text = st.text_area(
            "Content",
            height=200,
            placeholder="Paste content here...",
            key=f"content_{i}"
        )


        contents.append(
            {
                "source": source,
                "content_type": content_type,
                "date": date,
                "text": content_text
            }
        )


    # ------------------------------------------------
    # Analyze Contents
    # ------------------------------------------------

    if st.button("🔍 Analyze Contents"):

        incomplete = False


        for content_item in contents:

            if not content_item["text"].strip():

                incomplete = True
                break


        if incomplete:

            st.warning(
                "Please enter text for all content items "
                "before analyzing."
            )


        else:

            results = analyze_multiple_contents(
                contents,
                api_mode
            )


            # ------------------------------------------------
            # Comparison Dataset
            # ------------------------------------------------

            df = pd.DataFrame(
                results
            )


            st.subheader(
                "📊 Content Comparison"
            )


            st.dataframe(
                df,
                use_container_width=True
            )


            # ------------------------------------------------
            # Primary Frame Distribution
            # ------------------------------------------------

            st.subheader(
                "📈 Primary Frame Distribution"
            )

            frame_counts = (
                df["Primary Frame"]
                .value_counts()
                .rename_axis("Frame")
                .reset_index(name="Contents")
            )

            st.bar_chart(
                frame_counts,
                x="Frame",
                y="Contents",
                horizontal=True,
                use_container_width=True
            )

            # ------------------------------------------------
            # Sentiment Distribution
            # ------------------------------------------------

            st.subheader(
                "💭 Sentiment Distribution"
            )

            sentiment_counts = (
                df["Sentiment"]
                .value_counts()
                .rename_axis("Sentiment")
                .reset_index(name="Contents")
            )

            st.bar_chart(
                sentiment_counts,
                x="Sentiment",
                y="Contents",
                horizontal=True,
                use_container_width=True
            )

            # ------------------------------------------------
            # Search Intent Distribution
            # ------------------------------------------------

            st.subheader(
                "🔍 Search Intent Distribution"
            )

            intent_counts = (
                df["Search Intent"]
                .value_counts()
                .rename_axis("Search Intent")
                .reset_index(name="Contents")
            )

            st.bar_chart(
                intent_counts,
                x="Search Intent",
                y="Contents",
                horizontal=True,
                use_container_width=True
            )

            # ------------------------------------------------
            # Cross-Content Insights
            # ------------------------------------------------

            st.subheader(
                "💡 Cross-Content Insights"
            )

            # =================================================
            # Shared Topics
            # =================================================

            st.markdown(
                "### 🔗 Shared Topics"
            )

            topics = [
                topic
                for topic in df["Topic"].tolist()
                if isinstance(topic, str)
                   and topic.strip()
            ]

            if topics:

                # ------------------------------------------------
                # Semantic Topic Grouping
                # ------------------------------------------------

                topic_groups = group_similar_topics(
                    topics,
                    threshold=0.60
                )

                shared_groups = [
                    group
                    for group in topic_groups
                    if len(group) > 1
                ]

                if shared_groups:

                    for i, group in enumerate(
                            shared_groups,
                            1
                    ):

                        representative = (
                            get_representative_topic(
                                group
                            )
                        )

                        st.markdown(
                            f"**Topic Group {i}**"
                        )

                        st.write(
                            f"Representative Topic: "
                            f"**{representative}**"
                        )

                        for topic in group:
                            st.write(
                                f"- {topic}"
                            )

                        st.divider()

                else:

                    st.write(
                        "No semantically shared topics "
                        "were identified."
                    )

            else:

                st.write(
                    "No valid topics available."
                )


            # =================================================
            # Sentiment Pattern
            # =================================================

            st.markdown(
                "### 💭 Sentiment Pattern"
            )

            sentiment_counts = (
                df["Sentiment"]
                .value_counts()
            )

            dominant_sentiment = (
                sentiment_counts.idxmax()
            )

            dominant_count = (
                sentiment_counts.max()
            )

            total_contents = len(df)

            dominant_percentage = (
                    dominant_count /
                    total_contents *
                    100
            )

            st.write(
                f"The content set is predominantly "
                f"**{dominant_sentiment}**, with "
                f"{dominant_count} of {total_contents} "
                f"contents ({dominant_percentage:.0f}%)."
            )

            # =================================================
            # Framing Differences
            # =================================================

            st.markdown(
                "### 🧩 Framing Differences"
            )

            frame_by_type = pd.crosstab(
                df["Content Type"],
                df["Primary Frame"]
            )

            if not frame_by_type.empty:

                st.dataframe(
                    frame_by_type,
                    use_container_width=True
                )

            else:

                st.write(
                    "No framing differences available."
                )

            # =================================================
            # Content-Type Comparison
            # =================================================

            st.markdown(
                "### 📚 Content-Type Comparison"
            )

            type_summary = (
                df.groupby("Content Type")
                .agg(
                    Contents=("Content Type", "count"),
                    Dominant_Sentiment=(
                        "Sentiment",
                        lambda x: x.mode().iloc[0]
                        if not x.mode().empty
                        else "Unknown"
                    ),
                    Dominant_Frame=(
                        "Primary Frame",
                        lambda x: x.mode().iloc[0]
                        if not x.mode().empty
                        else "Unknown"
                    ),
                    Dominant_Intent=(
                        "Search Intent",
                        lambda x: x.mode().iloc[0]
                        if not x.mode().empty
                        else "Unknown"
                    )
                )
                .reset_index()
            )

            type_summary.columns = [
                "Content Type",
                "Contents",
                "Dominant Sentiment",
                "Dominant Frame",
                "Dominant Search Intent"
            ]

            st.dataframe(
                type_summary,
                use_container_width=True
            )
