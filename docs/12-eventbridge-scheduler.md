# Amazon EventBridge Scheduler

## 1. Overview

Amazon EventBridge Scheduler is used to run tasks automatically according to a defined schedule.

In this project, EventBridge Scheduler invokes the AWS Lambda function every five minutes to collect and process news articles.

## 2. Scheduler Configuration

| Configuration | Value |
|---|---|
| Schedule name | `news-sentiment-every-5-min` |
| Schedule expression | `rate(5 minutes)` |
| Time zone | `Asia/Kolkata` |
| Target service | AWS Lambda |
| Target function | `news-sentiment-lambda-container` |
| Input | `{}` |
| Status | Enabled |

## 3. Execution Workflow

The scheduled workflow operates as follows:

1. EventBridge Scheduler waits for the next scheduled execution.
2. Every five minutes, it invokes the configured Lambda function.
3. Lambda retrieves news articles from GNews