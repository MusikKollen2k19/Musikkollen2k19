import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def getData(): # Hämtar alla Items i databasen
    table = dynamodb.Table('Musikkollen')
    
    result =  table.scan()["Items"]
    
    # print(result)
    
    # Av någon anledning blir tal som t.ex 10 "Decimal('10')". 
    # detta fixar vi genom att konvertera allt till ints före vi skickar tillbaka dem
    for x in range(len(result)):
        # print(x)
    
        result[x]["CurrentAmount"] = int(result[x]["CurrentAmount"])
        
        for y in range(len(result[x]["LastAmount"])):
            result[x]["LastAmount"][y] = int(result[x]["LastAmount"][y])
    
    return result

def lambda_handler(event, context):
    # vi bryr oss inte om body nu
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
    
    # a = str().replace("Decimal('", "").replace("')","")
    
    # print(getData())
    # print(type(getData()))
    
    # print(json.loads(list(a)[0]))

    return {
        'statusCode': 200,
        'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*" 
        },
        'body': json.dumps(getData()) # str(getData()).replace("Decimal('", "").replace("')","")
    }
