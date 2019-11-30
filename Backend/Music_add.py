import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


def checkbody(body):

    if "pass" not in body:
        return [False, "pass"]

    if "user" not in body:
        return [False, "user"]

    if "Amount" not in body:
        return [False, "Amount"]

    if type(body["Amount"]) != int:
        return [False, "int"]

    return [True]


def checkpass(body):
    table = dynamodb.Table('Users')

    User = body["user"].lower()

    result = table.get_item(
        Key={
            'username': User,

        }
    )

    if "Item" not in result:  # avslutar om användaren inte finns
        return [False, "No user"]

    if result["Item"]["password"] == body["pass"]:  # om det stämmer överäns
        return [True]
    else:
        return [False, "No user"]


# Eftersom vi vet att användaren finns i User behöver vi bara kolla om den också finns i Musikkollen
def CrossReferenceShcool(body):
    table = dynamodb.Table('Musikkollen')

    User = body["user"].lower()

    result = table.scan()

    for x in result["Items"]:
        # print(x)
        if User in x["Ansvarig"]:
            return [True, x["Skola"]]

    return [False, "No user"]


def addto(body, Skola):

    table = dynamodb.Table('Musikkollen')

    result = table.get_item(
        Key={
            'Skola': Skola,
        }
    )

    currentAmount = result["Item"]["CurrentAmount"]

    # result["Item"]["LastAmount"][0] = int(result["Item"]["LastAmount"][0])
    result["Item"]["CurrentAmount"] = int(result["Item"]["CurrentAmount"])

    result["Item"]["LastAmount"].append(int(body["Amount"]))
    result["Item"]["LastUpdate"].append(str(datetime.datetime.now()))

    # print(result["Item"])

    response = table.put_item(
        Item={
            'Skola': Skola,
            'Ansvarig': result["Item"]["Ansvarig"],

            'LastUpdate': result["Item"]["LastUpdate"],
            'LastAmount': result["Item"]["LastAmount"],
            'CurrentAmount': (body["Amount"] + currentAmount),
        }
    )

    print(response)

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
    # TODO implement
    body = (event["body"])

    # print(type(checkbody(body)))

    if checkbody(body)[0] == False:  # Hittade inte Skola, id eller Amount

        if checkbody(body)[1] == "int":
            return {
                'statusCode': 201,
                'body': {
                    "Success": False,
                    "Meddelande": "'Amount' isn't a int!"
                }
            }

        return {
            'statusCode': 201,
            'body': {
                "Success": False,
                "Meddelande": "No '" + checkbody(body)[1] + "' in body!"
            }
        }

    check = checkpass(body)
    # print(check)

    if check[0] == False:  # Hittade inte användaren
        return {
            'statusCode': 201,
            'body': {
                "Success": False,
                "Meddelande": "HIttade inte användaren!"
            }
        }

    cross = CrossReferenceShcool(body)

    if cross[0] == False:  # Hittade inte den ansvarige
        return {
            'statusCode': 201,
            'body': {
                "Success": False,
                "Meddelande": "HIttade inte den ansvarige!"
            }
        }

    addto(body, cross[1])

    return {
        'statusCode': 200,
        'body': {
            "Success": True,
            "Meddelande": "Uppdaterade Värdet!"
        }
    }
