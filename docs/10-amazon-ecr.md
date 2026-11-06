# Amazon Elastic Container Registry (ECR)

## 1. Overview

Amazon Elastic Container Registry (ECR) is a managed AWS service used to store and manage Docker container images.

In this project, ECR stores the container images required to deploy the AWS Lambda function and Streamlit dashboard.

## 2. ECR Repositories

The project uses two separate ECR repositories:

| Repository | Purpose |
|---|---|
| `news-sentiment-lambda` | Stores the Lambda container image |
| `news-sentiment-dashboard` | Stores the Streamlit dashboard image |

## 3. Lambda Container Image

The Lambda application is packaged into a Docker image using the AWS Lambda Python base image.

The image is uploaded to:

```text
news-sentiment-lambda
```

AWS Lambda uses this image to execute the news-processing application.

## 4. Dashboard Container Image

The Streamlit dashboard is packaged into a separate Docker image.

The image is uploaded to:

```text
news-sentiment-dashboard
```

Amazon ECS with AWS Fargate uses this image to run the dashboard.

## 5. Image Deployment Workflow

The general container deployment workflow is:

1. Prepare the application and Dockerfile.
2. Build the Docker image locally.
3. Authenticate Docker with Amazon ECR.
4. Tag the image using the ECR repository URI.
5. Push the image to the appropriate ECR repository.
6. Configure Lambda or ECS to use the uploaded image.

## 6. Image Management

ECR provides a central location for storing container images.

Separate repositories help organize the Lambda and dashboard application images.

New image versions can be uploaded when application code or dependencies change.

## 7. Security Considerations

- Never include API keys or database passwords in container images.
- Keep AWS credentials outside the application source code.
- Use appropriate IAM permissions for image access.
- Avoid making private ECR repositories publicly accessible.

## 8. Summary

Amazon ECR connects the Docker build process with AWS deployment services