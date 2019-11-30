import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def getData():
    table = dynamodb.Table('Musikkollen')
    
    return table.scan()["Items"]

def lambda_handler(event, context):
    
    # try:
    #     body = json.loads(event)
    # except Exception:
    #     return {
    #         'statusCode': 201,
    #         'body': json.dumps({
    #             "Success": False,
    #             "Meddelande": "No body!"
    #         })
    #     }
    
    getData()

    return {
        'statusCode': 200,
        'body': json.dumps(str(getData()).replace("Decimal('", "").replace("')",""))
    }
