# Creates a DynamoDB table with 'id' as the partition key using Boto3

import boto3
from botocore.exceptions import ClientError

def create_table(table_name):
    dynamodb = boto3.client('dynamodb')
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print(f"\nCreating table '{table_name}'...")
        waiter = dynamodb.get_waiter('table_exists')
        waiter.wait(TableName=table_name)
        print("✅ Table created successfully.")
    except ClientError as e:
        print(f"Error: {e}")

# Replace with your table name
create_table('Boto3DemoTable')
