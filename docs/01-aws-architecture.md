# AWS Project Architecture – Real-Time News Sentiment Analysis

## 1. Project Overview

This project collects real-time technology news, analyzes the sentiment of each article, stores the results, and displays them through a web dashboard.

The solution uses AWS services, Python, PostgreSQL, Docker, and Streamlit.

## 2. Architecture Workflow

1. Amazon EventBridge Scheduler triggers the pipeline every five minutes.
2. AWS Lambda executes the Python application using a container image.
3. The application fetches technology news from the GNews API.
4. Raw news data is stored in Amazon S3 as JSON.
5. VADER analyzes the sentiment of each article.
6. Processed news articles are inserted into Amazon RDS PostgreSQL.
7. Amazon ECS with AWS Fargate hosts the Streamlit dashboard.
8. Users access the dashboard through a web browser.

## 3. AWS Services Used

| AWS Service | Purpose |
|---|---|
| AWS Lambda | Runs the news-processing application |
| Amazon S3 | Stores raw news JSON files |
| Amazon RDS | Stores processed news and sentiment results |
| Amazon ECS | Manages the dashboard container |
| AWS Fargate | Runs the dashboard without managing servers |
| Amazon ECR | Stores Docker container images |
| Amazon EventBridge Scheduler | Runs Lambda every five minutes |
| Amazon CloudWatch | Stores application logs |
| AWS IAM | Manages service permissions |

## 4. Technologies

- Python
- PostgreSQL
- Docker
- Streamlit
- GNews API
- VADER Sentiment Analysis
- Git and GitHub

## 5. Sentiment Classification

The VADER compound score determines the sentiment:

- Positive: compound score >= 0.05
- Negative: compound score <= -0.05
- Neutral: compound score between -0.05 and 0.05

## 6. AWS Region

The project is deployed in the AWS Asia Pacific (Sydney) region:

`ap-southeast-2`

## 7. Networking Note

This is an educational demonstration architecture. Some resources use public access to enable communication between services in the current design.

For production deployments, use private networking, restricted security group rules, and appropriate authentication.

## 8. Expected Result

The completed pipeline automatically collects news, analyzes sentiment, stores the results, and displays them on a Streamlit dashboard.