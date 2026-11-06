# Amazon S3 Integration

## 1. Overview

Amazon S3 is used to store raw news data collected from the GNews API in JSON format.

## 2. S3 Configuration

| Setting | Value |
|---|---|
| AWS Service | Amazon S3 |
| Bucket | `news-sentiment-raw-818947918215` |
| Region | `ap-southeast-2` |
| Format | JSON |

## 3. Data Storage Workflow

1. Lambda retrieves news from GNews.
2. The raw response is prepared as JSON.
3. The application connects to S3 using boto3.
4. The JSON file is uploaded to the configured bucket.
5. Files are organized by date and time.

## 4. S3 Object Structure

```text
raw-news/YYYY/MM/DD/HHMMSS.json
```

Example:

```text
raw-news/2026/11/06/120000.json
```

## 5. IAM Permissions

The Lambda execution role requires `s3:PutObject` permission to upload objects.

Permissions should be restricted to the required bucket and object path.

## 6. Benefits

- Preserves original news data.
- Supports future analysis.
- Maintains raw data separately from processed database records.
- Helps with troubleshooting and auditing.

## 7. Result

Amazon S3 provides storage for raw news JSON files collected by the automated pipeline.