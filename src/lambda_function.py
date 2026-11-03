from src.news.gnews import fetch_news
from src.news.processor import process_article
from src.database.insert_news import insert_article
from src.storage.s3 import upload_raw_news


def lambda_handler(event, context):
    print("Starting AWS Lambda news sentiment pipeline...")

    # Fetch news from GNews
    data = fetch_news(max_results=10)
    articles = data.get("articles", [])

    print(f"Articles received: {len(articles)}")

    # Upload raw GNews response to S3
    s3_key = upload_raw_news(data)
    print(f"Raw news uploaded to S3: {s3_key}")

    # Process and insert articles into RDS
    processed_count = 0

    for article in articles:
        processed_article = process_article(article)

        if not processed_article.get("id"):
            print("Skipping article without ID.")
            continue

        insert_article(processed_article)

        processed_count += 1

        print(
            f"Saved: {processed_article['title']} "
            f"| {processed_article['sentiment']} "
            f"| {processed_article['sentiment_score']}"
        )

    print(f"Pipeline completed. Articles processed: {processed_count}")

    return {
        "statusCode": 200,
        "message": f"Processed and inserted {processed_count} articles.",
        "s3_key": s3_key,
    }