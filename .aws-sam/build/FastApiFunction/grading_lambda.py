import json

def lambda_handler(event, context):
    assignments = event.get("assignments", [])
    avg_score = sum(a["score"] for a in assignments) / len(assignments)
    return {
        "statusCode": 200,
        "body": json.dumps({"average_score": avg_score})
    }
