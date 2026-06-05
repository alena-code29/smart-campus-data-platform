from pathlib import Path
import os
import tempfile

import boto3
import pandas as pd
from prefect import flow, task

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / 'data' / 'raw'
BRONZE_DIR = PROJECT_ROOT / 'data' / 'lake' / 'bronze' / 'learning_analytics'

S3_ENDPOINT = os.getenv('S3_ENDPOINT_URL', 'http://localhost:9000')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY', 'admin')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY', 'admin12345')
S3_BUCKET = os.getenv('S3_BUCKET', 'smart-campus-data-lake')

DATASETS = ['students', 'grades', 'attendance', 'lms_events']


def s3_client():
    return boto3.client(
        's3',
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
    )


@task(retries=3, retry_delay_seconds=5)
def ensure_bucket():
    client = s3_client()
    existing = [bucket['Name'] for bucket in client.list_buckets().get('Buckets', [])]
    if S3_BUCKET not in existing:
        client.create_bucket(Bucket=S3_BUCKET)
    return S3_BUCKET


@task(retries=2, retry_delay_seconds=3)
def read_csv_dataset(dataset_name: str) -> pd.DataFrame:
    path = RAW_DIR / f'{dataset_name}.csv'
    if not path.exists():
        raise FileNotFoundError(f'Missing source file: {path}')
    df = pd.read_csv(path)
    df['ingestion_source'] = f'csv:{dataset_name}'
    df['bronze_loaded_at'] = pd.Timestamp.utcnow().isoformat()
    return df


@task(retries=3, retry_delay_seconds=5)
def write_bronze(dataset_name: str, df: pd.DataFrame) -> str:
    BRONZE_DIR.mkdir(parents=True, exist_ok=True)
    local_path = BRONZE_DIR / f'{dataset_name}.parquet'
    df.to_parquet(local_path, index=False)

    key = f'bronze/learning_analytics/{dataset_name}/{dataset_name}.parquet'
    try:
        s3_client().upload_file(str(local_path), S3_BUCKET, key)
        return f's3://{S3_BUCKET}/{key}'
    except Exception as exc:
        print(f'Warning: S3 upload failed, local file is saved: {local_path}. Error: {exc}')
        return str(local_path)


@flow(name='smart-campus-load-raw-to-bronze')
def load_raw_to_bronze():
    ensure_bucket()
    outputs = []
    for dataset in DATASETS:
        df = read_csv_dataset(dataset)
        outputs.append(write_bronze(dataset, df))
    print('Bronze outputs:')
    for output in outputs:
        print(output)


if __name__ == '__main__':
    load_raw_to_bronze()
