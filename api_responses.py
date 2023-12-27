import json

def _200(data: dict = {}):
    return {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*"
        },
        "statusCode":200,
        "body": json.dumps(data)
    }
    
def _400(data: dict = {}):
    return {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*"
        },
        "statusCode":400,
        "body": json.dumps(data)
    }