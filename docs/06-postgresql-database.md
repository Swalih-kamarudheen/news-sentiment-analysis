# PostgreSQL Database Integration

## 1. Overview

PostgreSQL is used to store processed news articles and their sentiment analysis results.

The project uses Amazon RDS to host the PostgreSQL database in AWS.

## 2. Database Configuration

| Setting | Value |
|---|---|
| Database engine | PostgreSQL |
| Database name | `news_sentiment` |
| Table name | `news_articles` |
| Database username | `postgres` |
| Port | `5432` |
| AWS Region | `ap-southeast-2` |

The database password is stored securely as an environment variable and is not included in this documentation.

## 3. Database Connection

The Python application uses `psycopg2-binary` to connect to PostgreSQL.

Connection settings are supplied through environment variables:

- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

## 4. Article Data Structure

The `news_articles` table stores fields such as:

- Article ID
- Title
- Description
- Content
- Article URL
- Image URL
- Publication date
- Language
- Source name
- Source URL
- Source country
- Sentiment
- Sentiment score

## 5. Data Insertion

After sentiment analysis, processed articles are inserted into the database.

The application uses:

`ON CONFLICT (id) DO NOTHING`

This prevents duplicate article IDs from being inserted.

## 6. Database Security

- Database credentials must not be hardcoded.
- Use environment variables for connection settings.
- Restrict database access through security groups.
- Use encrypted connections and private networking for production deployments.

## 7. AWS Networking Note

The educational project uses a publicly accessible RDS instance because the Lambda function runs outside the VPC.

This is a demonstration configuration, not a recommended production security design. Production deployments should use private networking and restricted inbound rules.

## 8. Result

Amazon RDS PostgreSQL stores the processed news articles