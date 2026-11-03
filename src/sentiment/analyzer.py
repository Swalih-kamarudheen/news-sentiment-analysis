from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> tuple[str, float]:
    """
    Analyze the sentiment of the given text.

    Returns:
        tuple[str, float]:
            sentiment label and compound sentiment score.
    """

    if not text or not text.strip():
        return "neutral", 0.0

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "positive"
    elif compound <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, compound