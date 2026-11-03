# 📰 Real-Time News Sentiment Analysis using AWS

A cloud-based **near-real-time news sentiment analysis pipeline** that automatically collects technology news, analyzes sentiment using Python and VADER, stores raw and processed data, and displays the results through a Streamlit dashboard hosted on AWS.

---

## 📌 Project Overview

This project demonstrates how multiple AWS services can be integrated to build an automated data processing and visualization pipeline.

The system automatically runs every **5 minutes**, collects the latest technology news from the **GNews API**, performs sentiment analysis using **VADER**, stores the raw news in **Amazon S3**, stores processed articles in **Amazon RDS PostgreSQL**, and displays the results through a **Streamlit dashboard running on Amazon ECS Fargate**.

### 🔄 Architecture

```text
                    ┌─────────────────────┐
                    │ EventBridge Scheduler│
                    │     Every 5 Minutes  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    AWS Lambda       │
                    │  Container Image    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     GNews API       │
                    │  Technology News    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Python Processing   │
                    │ + VADER Sentiment   │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          ┌─────────────────┐   ┌────────────────────┐
          │   Amazon S3     │   │ Amazon RDS          │
          │   Raw JSON Data │   │ PostgreSQL          │
          └─────────────────┘   └─────────┬──────────┘
                                          │
                                          ▼
                              ┌────────────────────────┐
                              │ Amazon ECS Fargate      │
                              │ Streamlit Dashboard     │
                              └────────────────────────┘
```

### Architecture Diagram

![AWS Architecture](assets/dashboard.png.jpeg)

---

## 🚀 End-to-End Workflow

1. **EventBridge Scheduler** triggers the pipeline every 5 minutes.
2. **AWS Lambda** starts the news processing workflow.
3. Lambda calls the **GNews API** and retrieves technology-related news.
4. The raw API response is stored in **Amazon S3** as a JSON file.
5. Python processes each article.
6. **VADER Sentiment Analysis** calculates the sentiment score.
7. Each article is classified as:
   - 🟢 Positive
   - 🔴 Negative
   - ⚪ Neutral
8. Processed articles are stored in **Amazon RDS PostgreSQL**.
9. A **Streamlit dashboard** running on **Amazon ECS Fargate** reads the latest data from RDS.
10. The dashboard displays sentiment statistics and recent news articles.

---

## ☁️ AWS Services Used

| AWS Service                      | Purpose                                             |
| -------------------------------- | --------------------------------------------------- |
| **Amazon EventBridge Scheduler** | Automatically triggers the pipeline every 5 minutes |
| **AWS Lambda**                   | Executes the news processing pipeline               |
| **Amazon ECR**                   | Stores Docker container images                      |
| **Amazon S3**                    | Stores raw news JSON data                           |
| **Amazon RDS PostgreSQL**        | Stores processed news and sentiment data            |
| **Amazon ECS Fargate**           | Hosts the Streamlit dashboard                       |
| **AWS IAM**                      | Manages permissions and access                      |
| **Amazon CloudWatch**            | Stores Lambda/application logs                      |

---

## 🛠️ Technologies Used

- **Python 3.14**
- **VADER Sentiment Analysis**
- **GNews API**
- **PostgreSQL**
- **AWS**
- **Docker**
- **Amazon ECR**
- **AWS Lambda**
- **Amazon S3**
- **Amazon RDS**
- **Amazon ECS Fargate**
- **Amazon EventBridge**
- **Streamlit**
- **Git & GitHub**

---

## 🧠 Sentiment Analysis

The project uses the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** sentiment analyzer.

The VADER compound score ranges from **-1 to +1**.

|             Compound Score | Sentiment |
| -------------------------: | --------- |
|                  `>= 0.05` | Positive  |
|                 `<= -0.05` | Negative  |
| Between `-0.05` and `0.05` | Neutral   |

The sentiment score is stored in PostgreSQL along with the article information.

---

## 🗄️ Database

The project uses **Amazon RDS PostgreSQL**.

### Database

```text
news_sentiment
```

### Main Table

```text
news_articles
```

The table stores information such as:

- Article ID
- Title
- Description
- Content
- URL
- Image
- Published date
- Language
- Source
- Sentiment
- Sentiment score

The article ID is used as the primary key, and duplicate articles are prevented using:

```sql
ON CONFLICT (id) DO NOTHING
```

---

## 🪣 Amazon S3

Raw GNews API responses are stored in Amazon S3.

Objects follow a structure similar to:

```text
raw-news/
└── YYYY/
    └── MM/
        └── DD/
            └── HHMMSS.json
```

This keeps the original API response available for future analysis or auditing.

---

## 🐳 Docker

Docker is used to containerize the application.

Two Docker images are used:

### Lambda

```text
news-sentiment-lambda
```

The Lambda container contains the Python news processing pipeline.

### Dashboard

```text
news-sentiment-dashboard
```

The dashboard container runs the Streamlit application on port:

```text
8501
```

---

## 📊 Streamlit Dashboard

The dashboard displays:

- Total number of articles
- Positive article count
- Negative article count
- Neutral article count
- Sentiment distribution
- Recent news articles
- Sentiment scores
- Source information
- Clickable article links

The dashboard is deployed using **Amazon ECS Fargate**.

---

## 📁 Project Structure

```text
news-sentiment-analysis/
│
├── dashboard/
│   ├── app.py
│   └── Dockerfile
│
├── src/
│   ├── database/
│   │   ├── connection.py
│   │   ├── insert_news.py
│   │   └── tables.py
│   │
│   ├── news/
│   │   ├── gnews.py
│   │   └── processor.py
│   │
│   ├── sentiment/
│   │   └── analyzer.py
│   │
│   ├── storage/
│   │   └── s3.py
│   │
│   ├── lambda_function.py
│   └── local_pipeline.py
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔐 Security

Sensitive information is **not stored in the GitHub repository**.

Environment variables are used for:

```text
GNEWS_API_KEY
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
S3_BUCKET
```

The `.env` file is excluded using `.gitignore`.

AWS credentials and API keys should never be committed to GitHub.

---

## 🧪 Testing

The project was tested in stages:

1. GNews API connection
2. VADER sentiment analysis
3. PostgreSQL/RDS connection
4. S3 upload
5. Complete local pipeline
6. Lambda Docker container
7. AWS Lambda execution
8. Lambda → RDS connection
9. EventBridge → Lambda automation
10. Local Streamlit dashboard
11. ECS Fargate deployment
12. ECS → RDS connection
13. Complete end-to-end pipeline

---

## 📈 Project Result

The completed system can automatically:

**Collect → Process → Analyze → Store → Visualize**

technology news without manually running the pipeline every time.

The final workflow is:

```text
EventBridge
     ↓
AWS Lambda
     ↓
GNews API
     ↓
Python + VADER
     ↓
 ┌───────────┐
 ↓           ↓
S3          RDS
             ↓
        ECS Fargate
             ↓
     Streamlit Dashboard
```

---

## 🔮 Future Improvements

For a production environment, the architecture could be improved by:

- Moving RDS into a private subnet
- Removing public database access
- Using tighter security-group rules
- Adding HTTPS using an Application Load Balancer
- Adding authentication to the dashboard
- Using AWS Secrets Manager instead of plain environment variables
- Adding CI/CD with GitHub Actions
- Adding monitoring and alerting
- Implementing better scaling and fault tolerance

---

## 👨‍💻 Author

**Swalih Kamarudheen**

GitHub:
[https://github.com/Swalih-kamarudheen](https://github.com/Swalih-kamarudheen)

---

## ⭐ Project Summary

This project demonstrates practical experience with:

**Python • AWS • Docker • PostgreSQL • Lambda • S3 • RDS • ECS Fargate • EventBridge • ECR • Streamlit • Git • GitHub**

It combines **data ingestion, sentiment analysis, cloud computing, containerization, database management, automation, and data visualization** into a single end-to-end project.
