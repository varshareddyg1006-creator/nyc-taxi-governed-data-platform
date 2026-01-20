import os
import sys
import boto3
from botocore.exceptions import ClientError

BUCKET = "task6-varsha-datalake"
PREFIX = "landing-raw/"

# Change these to your local file paths when running locally
FILES = [
    ("taxi_zone_lookup.csv", "taxi_zone_lookup.csv"),
    ("yellow_tripdata_2025-08.parquet", "yellow_tripdata_2025-08.parquet"),
]

TAGS = {
    "owner": "data-engineering",
    "steward": "analytics",
    "domain": "transportation",
    "classification": "internal"
}

def to_tagging_header(tags: dict) -> str:
    # S3 expects URL-encoded key=value&key=value
    parts = []
    for k, v in tags.items():
        parts.append(f"{k}={v}")
    return "&".join(parts)

def upload_and_tag(s3_client, local_path: str, s3_key: str):
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"Local file not found: {local_path}")

    print(f"Uploading: {local_path} -> s3://{BUCKET}/{s3_key}")
    s3_client.upload_file(
        Filename=local_path,
        Bucket=BUCKET,
        Key=s3_key,
        ExtraArgs={
            "Tagging": to_tagging_header(TAGS)
        }
    )

    # Verify
    head = s3_client.head_object(Bucket=BUCKET, Key=s3_key)
    size = head.get("ContentLength", None)
    print(f"Verified: s3://{BUCKET}/{s3_key} size={size} bytes")

def main():
    # Uses your configured AWS creds (AWS CLI, env vars, or IAM role)
    s3_client = boto3.client("s3")

    for local_file, remote_name in FILES:
        s3_key = f"{PREFIX}{remote_name}"
        upload_and_tag(s3_client, local_file, s3_key)

    print("\nDone. Uploaded + tagged + verified all files.")

if __name__ == "__main__":
    try:
        main()
    except ClientError as e:
        print("AWS ClientError:", e)
        sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
