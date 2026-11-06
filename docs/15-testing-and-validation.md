# Testing and Validation

## 1. Overview

Testing and validation ensure that each component of the Real-Time News Sentiment Analysis project works correctly.

The project should be tested step by step before running the complete AWS pipeline.

## 2. Testing Order

The recommended testing sequence is:

| Step | Component | Validation |
|---|---|---|
| 1 | GNews API | Retrieve news articles successfully |
| 2 | VADER | Calculate sentiment scores |
| 3 | PostgreSQL | Connect and insert records |
| 4 | Amazon S3 | Upload raw JSON data |
| 5 | Local pipeline | Execute the complete local workflow |
| 6 | Docker | Build and test the Lambda image |
| 7 | AWS Lambda | Execute the deployed function |
| 8 | Lambda to RDS | Verify database connectivity |
| 9 | EventBridge | Verify scheduled Lambda invocation |
| 10 | Local Streamlit | Open the dashboard locally |
| 11 | ECS Fargate | Verify dashboard container deployment |
| 12 | ECS to RDS | Verify dashboard database connectivity |
| 13 | End-to-end | Validate the complete application |

## 3. GNews API Testing

Verify that the application can retrieve articles from the GNews API.

Check:

- API key is configured correctly.
- API request