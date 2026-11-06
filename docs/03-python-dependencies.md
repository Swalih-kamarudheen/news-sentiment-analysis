# Python Dependencies and Project Configuration

## 1. Overview

Python libraries are used to connect external services, process news articles, analyze sentiment, store data, and run the dashboard.

## 2. Main Python Dependencies

| Library | Purpose |
|---|---|
| requests | Send HTTP requests to the GNews API |
| vaderSentiment | Analyze news sentiment |
| psycopg2-binary | Connect Python to PostgreSQL |
| boto3 | Interact with AWS services such as S3 |
| python-dotenv | Load environment variables from `.env` |
| streamlit | Build the web dashboard |
| pandas | Organize and display tabular data |

The exact installed versions are maintained in the project's `requirements.txt` file.

## 3. Dependency Installation

Activate the project's virtual environment and install the dependencies:

```powershell
pip install -r requirements.txt
```

To check installed packages:

```powershell
pip list
```

## 4. Project Configuration

Application settings and credentials are provided through environment variables.

The `.env` file is used for local development. It should not be committed to GitHub.

Example variable names:

```env
GNEWS_API_KEY=your_api_key
DB_HOST=your_database_endpoint
DB_PORT=5432
DB_NAME=news_sentiment
DB_USER=postgres
DB_PASSWORD=your_database_password
```

These are placeholders only. Never put real credentials in documentation or public repositories.

## 5. Configuration Best Practices

- Keep credentials outside the source code.
- Use `.gitignore` to exclude `.env`.
- Use environment variables in local and AWS environments.
- Install dependencies from `requirements.txt`.
- Avoid unnecessary packages.

## 6. Result

The project dependencies and configuration support the news collection, sentiment analysis, database, AWS integration, and dashboard components.