import os

import requests
from dotenv import load_dotenv


load_dotenv()

GNEWS_API_URL = "https://gnews.io/api/v4/search"


def fetch_news(query: str = "technology", max_results: int = 10) -> dict:
    """Fetch news articles from GNews."""

    api_key = os.getenv("GNEWS_API_KEY")

    if not api_key:
        raise ValueError("GNEWS_API_KEY is not configured.")

    params = {
        "q": query,
        "lang": "en",
        "max": max_results,
        "apikey": api_key,
    }

    response = requests.get(
        GNEWS_API_URL,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()