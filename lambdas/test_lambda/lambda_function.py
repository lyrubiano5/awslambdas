import json


def lambda_handler(event, context):
    # TODO implement
    if event["key1"] == "value1":
        return {
            'statusCode': 201,
            'body': json.dumps('Value 1 created')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
