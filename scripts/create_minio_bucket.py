import os
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.getenv('S3_ENDPOINT_URL', 'http://localhost:9000')
ACCESS_KEY = os.getenv('S3_ACCESS_KEY', 'admin')
SECRET_KEY = os.getenv('S3_SECRET_KEY', 'admin12345')
BUCKET = os.getenv('S3_BUCKET', 'smart-campus-data-lake')

s3 = boto3.client(
    's3',
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

try:
    s3.create_bucket(Bucket=BUCKET)
    print(f'Bucket created: {BUCKET}')
except ClientError as exc:
    code = exc.response.get('Error', {}).get('Code')
    if code in {'BucketAlreadyOwnedByYou', 'BucketAlreadyExists'}:
        print(f'Bucket already exists: {BUCKET}')
    else:
        raise
