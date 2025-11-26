import boto3
import random
import json

dynamodb = boto3.client("dynamodb")

def handler(event, context):
    response = dynamodb.scan(TableName="CloudFunFacts")
    items = response.get("Items", [])

    facts = [item["fact"]["S"] for item in items]
    random_fact = random.choice(facts)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
        },
        "body": json.dumps({"fact": random_fact})
    }
