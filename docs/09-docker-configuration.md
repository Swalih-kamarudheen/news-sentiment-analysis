# Docker Configuration

## 1. Overview

Docker is used to package the application and its dependencies into container images. These images provide consistent environments for running the Lambda function and Streamlit dashboard.

The project uses separate Docker configurations for:

- AWS Lambda container image
- Streamlit dashboard container image

## 2. Docker for AWS Lambda

The Lambda function is packaged using the AWS Lambda Python base image.

Base image:

```dockerfile
FROM public.ecr.aws/lambda/python:3.13
```

The Lambda container includes the Python runtime and application dependencies required to process news articles.

The configured handler is:

```text
src.lambda_function.lambda_handler
```

## 3. Docker for the Streamlit Dashboard

A separate Docker image is used