from src.database.connection import get_connection


def insert_article(article: dict) -> None:
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            query = """
                INSERT INTO news_articles (
                    id,
                    title,
                    description,
                    content,
                    url,
                    image,
                    published_at,
                    language,
                    source_name,
                    source_url,
                    source_country,
                    sentiment,
                    sentiment_score
                )
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s
                )
                ON CONFLICT (id) DO NOTHING;
            """

            values = (
                article.get("id"),
                article.get("title"),
                article.get("description"),
                article.get("content"),
                article.get("url"),
                article.get("image"),
                article.get("published_at"),
                article.get("language"),
                article.get("source_name"),
                article.get("source_url"),
                article.get("source_country"),
                article.get("sentiment"),
                article.get("sentiment_score"),
            )

            cursor.execute(query, values)

        conn.commit()

    finally:
        conn.close()