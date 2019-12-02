import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


def checkbody(body): # Kollar så att det finns pass, user, amount och att det är ett nummer

    if "pass" not in body:
        return [False, "pass"] # [status, anledning]

    if "user" not in body:
        return [False, "user"]

    if "Amount" not in body:
        return [False, "Amount"]

    if type(body["Amount"]) != int:
        return [False, "int"]

    return [True]


def checkpass(body): # Kolla så att lösenordet stämmer
    table = dynamodb.Table('Users')

    User = body["user"].lower() # Alla användarnamn har små bokstäver

    result = table.get_item(
        Key={
            'username': User,

        }
    )

    if "Item" not in result:  # avslutar om användaren inte finns eftersom Item ite finns
        return [False, "No user"]

    if result["Item"]["password"] == body["pass"]:  # om det stämmer överäns
        return [True]
    else:
        return [False, "No user"]


# Eftersom vi vet att användaren finns i User behöver vi bara kolla om den också finns i Musikkollen
def CrossReferenceShcool(body):
    table = dynamodb.Table('Musikkollen')

    User = body["user"].lower()

    result = table.scan() # Scannar hela table

    for x in result["Items"]: # kollar alla Items
        # print(x)
        if User in x["Ansvarig"]: # om user är ansvarig skickar den tillbaka den skolan
            return [True, x["Skola"]]

    return [False, "No user"] # om den inte har hittat säger den det


def addto(body, Skola): # Update expressions var jobbiga så vi hämtar allt, uppdaterar det och skickar tillbaka

    table = dynamodb.Table('Musikkollen')

    result = table.get_item(
        Key={
            'Skola': Skola, # Skola är huvudnyckeln så man måste söka efter det
        }
    )

    currentAmount = result["Item"]["CurrentAmount"]

    # result["Item"]["LastAmount"][0] = int(result["Item"]["LastAmount"][0])
    result["Item"]["CurrentAmount"] = int(result["Item"]["CurrentAmount"])

    result["Item"]["LastAmount"].append(int(body["Amount"])) # Lägger till allt nytt
    result["Item"]["LastUpdate"].append(str(datetime.datetime.now()))

    # print(result["Item"])

    table.put_item( # Skickar tillbaka
        Item={
            'Skola': Skola,
            'Ansvarig': result["Item"]["Ansvarig"],

            'LastUpdate': result["Item"]["LastUpdate"],
            'LastAmount': result["Item"]["LastAmount"],
            'CurrentAmount': (body["Amount"] + currentAmount),
        }
    )

    # print(response)

    # response = table.update_item(
    #     Key={
    #         'Skola': Skola,
    #     },
    #     # Här nedan har vi UpdateExpression, där säger vi vilka attribut i objektet som ska länkas till vilka bokstäver.
    #     UpdateExpression="set   #t = list_append(#t, :y), #u = list_append(#u, :o), LastUpdate=:u, CurrentAmount= :t,",
    #     ExpressionAttributeNames = {         # Dessa attribut är de som kommer att ändras.
    #         "#t": "LastAmount",
    #         "#u": "UpdatedAt",
    #     },
    #     ExpressionAttributeValues = {         # Dessa värden är de som kommer att ändras/läggas till.
    #         ":y": [body["Amount"]], # [] runt värdet gör det till en lista, detta behövs då list_append tar bara emot listor och sammanfogar dem.
    #         ":o": [str(datetime.datetime.now())],
    #         ":t": (body["Amount"] + currentAmount),
    #         ":u": str(datetime.datetime.now()),
    #     },
    #     ReturnValues = "UPDATED_NEW", # Man skickar ett returnvalue för att den ska veta att den ska uppdateras.
    # )


def handler(event, context):
    
    # print("\n", event, "\n"*2, type(event), "\n"*2)
    try:
        body = json.loads(event["body"])
    except Exception: # om body inte finns
        return {
            'statusCode': 201,
            'headers': {
                    'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "*" 
            },
            'body': json.dumps({
                "Success": False,
                "Meddelande": "No body!"
            })
        }
        
    
    

    # print(type(checkbody(body)))

    if checkbody(body)[0] == False:  # Hittade inte Skola, id eller Amount

        if checkbody(body)[1] == "int":
            return {
                'statusCode': 201,
                'headers': {
                        'Content-Type': 'application/json',
                        "Access-Control-Allow-Origin": "*" 
                },
                'body': json.dumps({
                    "Success": False,
                    "Meddelande": "'Amount' isn't a int!"
                })
            }

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

    check = checkpass(body)
    # print(check)

    if check[0] == False:  # Hittade inte användaren
        return {
            'statusCode': 201,
            'headers': {
                    'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "*" 
            },
            'body': json.dumps({
                "Success": False,
                "Meddelande": "HIttade inte användaren!"
            })
        }

    cross = CrossReferenceShcool(body)

    if cross[0] == False:  # Hittade inte den ansvarige
        return {
            'statusCode': 201,
            'headers': {
                    'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "*" 
            },
            'body': json.dumps({
                "Success": False,
                "Meddelande": "HIttade inte den ansvarige!"
            })
        }

    addto(body, cross[1]) # body och skola

    return {
        'statusCode': 200,
        'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*" 
        },
        'body': json.dumps({
            "Success": True,
            "Meddelande": "Uppdaterade Värdet!"
        })
    }
