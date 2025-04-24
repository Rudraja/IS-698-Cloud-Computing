# Inserts a sample item into the specified DynamoDB table using Boto3

import boto3
from botocore.exceptions import ClientError

def insert_item(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    try:
        response = table.put_item(
            Item={
                'id': '001',
                'name': 'TestItem',
                'category': 'Demo'
            }
        )
        print(f"\n✅ Item inserted successfully into '{table_name}'.")
    except ClientError as e:
        print(f"Error: {e}")

# Replace with your table name
insert_item('Boto3DemoTable')
