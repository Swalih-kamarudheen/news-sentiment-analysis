from src.news.gnews import fetch_news
from src.news.processor import process_article
from src.database.insert_news import insert_article
from src.storage.s3 import upload_raw_news


def run_pipeline():
    print("Starting news sentiment pipeline...")

    # Fetch news from GNews
    data = fetch_news(max_results=10)
    articles = data.get("articles", [])

    print(f"Articles received: {len(articles)}")

    # Store the original GNews response in S3
    s3_key = upload_raw_news(data)
    print(f"Raw news uploaded to S3: {s3_key}")

    # Process and store articles in RDS
    inserted = 0

    for article in articles:
        processed_article = process_article(article)

        if not processed_article.get("id"):
            print("Skipping article without ID.")
            continue

        insert_article(processed_article)

        inserted += 1

        print(
            f"Saved: {processed_article['title']} "
            f"| {processed_article['sentiment']} "
            f"| {processed_article['sentiment_score']}"
        )

    print(f"\nPipeline completed. Articles processed: {inserted}")


if __name__ == "__main__":
    run_pipeline()