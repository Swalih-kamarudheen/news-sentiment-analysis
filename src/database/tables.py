from src.database.connection import get_connection


def create_tables():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS news_articles (
                    id TEXT PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    content TEXT,
                    url TEXT,
                    image TEXT,
                    published_at TIMESTAMPTZ,
                    language TEXT,
                    source_name TEXT,
                    source_url TEXT,
                    source_country TEXT,
                    sentiment TEXT,
                    sentiment_score DOUBLE PRECISION
                );
                """
            )

        conn.commit()
        print("RDS TABLE CREATED SUCCESSFULLY")

    finally:
        conn.close()


if __name__ == "__main__":
    create_tables()