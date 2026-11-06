# Amazon ECS Fargate Deployment

## 1. Overview

Amazon Elastic Container Service (ECS) is a container orchestration service used to deploy and manage containerized applications.

AWS Fargate is a serverless compute engine for running containers without managing EC2 instances.

In this project, ECS Fargate runs the Streamlit news sentiment dashboard.

## 2. ECS Configuration

| Configuration | Value |
|---|---|
| Cluster name | `news-sentiment-cluster` |
| Service name | `news-sentiment-dashboard-service` |
| Task definition family | `news-sentiment-dashboard` |
| Launch type | Fargate |
| Operating system | Linux |
| CPU architecture | x86_64 |
| CPU | 0.25 vCPU |
| Memory | 0.5 GB |
| Desired tasks | 1 |

## 3. Container Image

The dashboard Docker image is stored in Amazon ECR:

```text
news-sentiment-dashboard
```

The ECS task definition references this image to run the Streamlit application.

## 4. Networking Configuration

The dashboard service uses the project's configured networking setup.

Important settings include:

- Public IP assignment enabled.
- Dashboard security group: `news-sentiment-dashboard-sg`.
- Inbound TCP port: `8501`.
- The