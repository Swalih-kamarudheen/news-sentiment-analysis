# Streamlit Dashboard

## 1. Overview

Streamlit is a Python framework used to build interactive web applications.

In this project, Streamlit provides a dashboard for viewing news articles and their sentiment analysis results stored in PostgreSQL.

## 2. Application Structure

The dashboard application is located at:

```text
dashboard/app.py
```

The application connects to the PostgreSQL database and retrieves processed news articles for display.

## 3. Dashboard Features

The dashboard is designed to display:

- Collected news articles.
- Article titles and descriptions.
- News sources and publication dates.
- Sentiment classifications.
- Sentiment scores.
- A summary of positive, negative, and neutral articles.

## 4. Database Connection

The dashboard uses PostgreSQL as its data source.

The main database configuration is provided through environment variables:

| Variable | Purpose |
|---|---|
| `DB_HOST` | PostgreSQL endpoint |
| `DB_PORT` | Database port (`5432`) |
| `DB_NAME` | Database name (`news_sentiment`) |
| `DB_USER` | Database username |
| `DB_PASSWORD` | Database password |

Credentials must be configured securely and must not be hardcoded in the application.

## 5. Streamlit Port Configuration

The application runs on port:

```text
8501
```

The Streamlit server must bind to:

```text
0.0.0.0
```

This allows the dashboard to be accessed from outside its container.

## 6. Local Execution

During local development, the dashboard can be accessed through:

```text
http://localhost:8501
```

The PostgreSQL database must be reachable and the required environment variables must be configured.

## 7. AWS