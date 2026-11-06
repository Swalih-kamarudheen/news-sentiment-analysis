# Local Pipeline Execution

## 1. Overview

Before deploying the application to AWS Lambda, the news sentiment pipeline can be tested locally.

Local testing helps verify API connectivity, data processing, sentiment analysis, S3 uploads, and PostgreSQL database insertion.

## 2. Pipeline Workflow

The local pipeline follows these stages:

1. Load configuration from environment variables.
2. Connect to the GNews API.
3. Retrieve technology news articles.
4. Upload the raw JSON response to Amazon S3.
5. Process the collected articles.
6. Analyze sentiment using VADER.
7. Connect to PostgreSQL.
8. Insert processed articles into the database.

## 3. Environment Configuration

Make sure the local `.env` file contains the required configuration:

- `GNEWS_API_KEY`
- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

Never share or commit the actual credentials.

## 4. Dependency Installation

Activate the virtual environment and install dependencies:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 5. Testing Strategy

Test each component independently before running the complete pipeline:

- GNews API request
- VADER sentiment analysis
- PostgreSQL connection
- Amazon S3 upload
- Complete local