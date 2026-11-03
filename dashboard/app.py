import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from src.database.connection import get_connection

load_dotenv()

st.set_page_config(
    page_title="News Sentiment Dashboard",
    page_icon="📰",
    layout="wide",
)

st.title("📰 Real-Time News Sentiment Analysis")
st.caption("AWS-powered news sentiment dashboard")


@st.cache_data(ttl=60)
def load_news():
    conn = get_connection()

    try:
        query = """
            SELECT
                id,
                title,
                source_name,
                sentiment,
                sentiment_score,
                published_at,
                url
            FROM news_articles
            ORDER BY published_at DESC
            LIMIT 100;
        """

        return pd.read_sql_query(query, conn)

    finally:
        conn.close()


df = load_news()

if df.empty:
    st.warning("No news articles found in the database.")
    st.stop()


# Metrics
total_articles = len(df)
positive_count = (df["sentiment"] == "positive").sum()
negative_count = (df["sentiment"] == "negative").sum()
neutral_count = (df["sentiment"] == "neutral").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Articles", total_articles)
col2.metric("Positive", positive_count)
col3.metric("Negative", negative_count)
col4.metric("Neutral", neutral_count)


st.divider()

# Sentiment distribution
st.subheader("Sentiment Distribution")

sentiment_counts = df["sentiment"].value_counts()

st.bar_chart(sentiment_counts)


st.divider()

# Recent news
st.subheader("Recent News")

display_df = df[
    [
        "title",
        "source_name",
        "sentiment",
        "sentiment_score",
        "published_at",
        "url",
    ]
].copy()

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "url": st.column_config.LinkColumn(
            "Article",
            display_text="Open Article",
        )
    },
)