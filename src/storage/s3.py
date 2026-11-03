import json
import os
from datetime import datetime, timezone

import boto3
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET = os.getenv("S3_BUCKET")

s3_client = boto3.client("s3")


def upload_raw_news(data: dict) -> str:
    timestamp = datetime.now(timezone.utc)

    key = f"raw-news/{timestamp:%Y/%m/%d/%H%M%S}.json"

    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=json.dumps(data, ensure_ascii=False).encode("utf-8"),
        ContentType="application/json",
    )

    return key