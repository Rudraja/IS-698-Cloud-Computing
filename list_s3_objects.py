import boto3
from botocore.exceptions import ClientError

def list_objects(bucket_name):
    s3 = boto3.client('s3', region_name='us-east-1')  # Ensure region matches your S3 bucket region
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        print(f"\nFiles in S3 bucket '{bucket_name}':")
        for obj in response.get('Contents', []):
            print(f" - {obj['Key']}")
    except ClientError as e:
        print(f"Error: {e}")

# Replace with your actual bucket name
list_objects('infrastack-bucket-us-east-1')

