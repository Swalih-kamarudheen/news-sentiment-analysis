# AWS Lambda Deployment

## 1. Overview

AWS Lambda is a serverless compute service that runs application code without requiring the management of servers.

In this project, Lambda processes news articles retrieved from the GNews API, stores raw responses in Amazon S3, performs sentiment analysis, and inserts processed articles into PostgreSQL.

## 2. Lambda Function Configuration

The project uses a container-image-based Lambda function.

| Configuration | Value |
|---|---|
| Function name | `news-sentiment-lambda-container` |
| Runtime base image | Python 3.13 |
| Architecture | x86_64 |
| Handler | `src.lambda_function.lambda_handler` |
| Region | `ap-southeast-2` (Sydney) |
| Timeout | At least 1 minute |

## 3. Container Image

The Lambda application is packaged using the AWS Lambda Python 3.13 base image.

The container image is stored in the Amazon ECR repository:

```text
news-sentiment-lambda
```

Lambda