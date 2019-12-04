import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def checkbody(body): # Kollar så att det finns pass, user, amount och att det är ett nummer

    if "Skola" not in body:
        return [False, "Skola"] # [status, anledning]

    if "Ansvarig" not in body:
        return [False, "Ansvarig"]

    return [True]

def checkthething(body):
    table = dynamodb.Table('Musikkollen')

    result = table.scan()

    print(body["Skola"])

    for x in result["Items"]:
        if body["Skola"] == x["Skola"]:
            return [False, "Skolan finns redan registrerad"]

    return [True]


def dothething(body):

    table = dynamodb.Table('Musikkollen')

    table.put_item(  # Skickar tillbaka
        Item={
            'Skola': body["Skola"],
            'Ansvarig': body["Ansvarig"],

            'LastUpdate': [],
            'LastAmount': [],
            'CurrentAmount': 0,
        }
    )


def handler(event, context):

    print("\n", event, "\n"*2, type(event), "\n"*2)
    try:
        body = json.loads(event["body"])
    except Exception:
        return {
            'statusCode': 201,
            'headers': {
                    'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                "Success": False,
                "Meddelande": "No body!",
                "Debug": event
            })
        }
    # body = event["body"]

    if checkbody(body)[0] == False:  # Hittade inte Skola, id eller Amount

        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*" 
            },
            'body': json.dumps({
                "Success": False,
                "Meddelande": "No '" + checkbody(body)[1] + "' in body!"
            })
        }

    check = checkthething(body)

    if check[0] == False:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({
                "Success": False,
                "Meddelande": check[1]
            })
        }

    dothething(body)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({
            "Success": True,
            "Meddelande": " Lade till skolan!"
        })
    }
