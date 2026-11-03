from src.sentiment.analyzer import analyze_sentiment


def process_article(article: dict) -> dict:
    """Extract useful fields and calculate sentiment."""

    title = article.get("title") or ""
    description = article.get("description") or ""
    content = article.get("content") or ""

    text_for_sentiment = " ".join(
        part for part in [title, description, content] if part
    )

    sentiment, sentiment_score = analyze_sentiment(text_for_sentiment)

    source = article.get("source") or {}

    return {
        "id": article.get("id"),
        "title": title,
        "description": description,
        "content": content,
        "url": article.get("url"),
        "image": article.get("image"),
        "published_at": article.get("publishedAt"),
        "language": article.get("language"),
        "source_name": source.get("name"),
        "source_url": source.get("url"),
        "source_country": source.get("country"),
        "sentiment": sentiment,
        "sentiment_score": sentiment_score,
    }