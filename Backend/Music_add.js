const AWS = require('aws-sdk');
const docClient = new AWS.DynamoDB.DocumentClient({
    region: 'us-east-1'
});


function checkid(e, callback) {

    let scanningParameters = {
        TableName: 'Users',
        Limit: 100
    }

    if (e.body) {
        // console.log(e)
        // const body = JSON.parse(e.body); //Avaktivera Jsonparse om du testar i lambda
        const body = (e.body);

        docClient.scan(scanningParameters, function (err, data) {
            if (err) {
                callback(err, null);
            }
            else {

                for (var i = 0; i < data.Items.length; i++) {
                    // console.log(i)
                    // console.log(data.Items[i])
                    if (data.Items[i].id == body.id) {
                        let currentuser = data.Items[i].username
                        console.log("Rätt ID! Username:", currentuser)

                        return (currentuser);


                    } else {

                        return (false);
                    }
                }



            }
        });


    }
}


exports.handler =  async function(e, ctx, callback) {

    // const body = JSON.parse(e.body); //Avaktivera Jsonparse om du testar i lambda
    const body = (e.body);


    if (!body.hasOwnProperty("Skola")) { // Måste ha ett Namn i body
        callback(null, {
            statusCode: 400, // Bad Request
            headers: {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*" // Required for CORS support to work
            },
            body: JSON.stringify({
                message: "No 'Skola' provided."
            })
        });
        return false;
    }

    if (!body.hasOwnProperty("id")) { // Måste ha ett id i body
        callback(null, {
            statusCode: 400, // Bad Request
            headers: {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*" // Required for CORS support to work
            },
            body: JSON.stringify({
                message: "No 'id' provided."
            })
        });
        return false;
    }

    const check = await checkid(e, callback)
    console.log(check)

    if (!checkid(e, callback) == false) {

        if (!body.hasOwnProperty("Amount")) { // måste ha amont i body
            callback(null, {
                statusCode: 400, // Bad Request
                headers: {
                    'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "*" // Required for CORS support to work
                },
                body: JSON.stringify({
                    message: "Need 'Amount' in body."
                })
            });
            return false;
        }



        console.log(e);

        var res = JSON.parse(JSON.stringify(body.Skola, function (a, b) {
            return typeof b === "string" ? b.toLowerCase() : b
        }));

        var params = {

            TableName: "TempData",

            Key: { //Lägger in nyckelvärdena 

                "Skola": res

            },

            //Här nedan har vi UpdateExpression, där säger vi vilka attribut i objektet som ska länkas till vilka bokstäver. 
            UpdateExpression: "set   #t = list_append(#t, :y), #u = list_append(#u, :o), LastUpdate=:u, CurrentAmount= :h",
            ExpressionAttributeNames: {         //Dessa attribut är de som kommer att ändras. 
                "#t": "Amount",
                "#u": "UpdatedAt",
            },
            ExpressionAttributeValues: {         //Dessa värden är de som kommer att ändras/läggas till. 
                ":y": [body.Amount], //[] runt värdet gör det till en lista, detta behövs då list_append tar bara emot listor och sammanfogar dem.
                ":o": [new Date().toUTCString()],
                ":t": body.Amount,
                ":u": new Date().toUTCString()
            },
            ReturnValues: "UPDATED_NEW" //Man skickar ett returnvalue för att den ska veta att den ska uppdateras. 

        };

        console.log("Updating the item...");

        docClient.putItem(params, function (err, data) {
            if (err) {
                const response = {
                    statusCode: 400,
                    headers: {
                        'Content-Type': 'application/json',
                        "Access-Control-Allow-Origin": "*" // Required for CORS support to work
                    },
                    body: JSON.stringify('Gick inte att uppdatera, försök igen eller titta på datan du skickar!'),
                };
                callback(err, response);
            } else {

                const response = {
                    headers: {
                        'Content-Type': 'application/json',
                        "Access-Control-Allow-Origin": "*" // Required for CORS support to work
                    },
                    statusCode: 200,
                    body: JSON.stringify(res + ' är uppdaterad!'),
                };
                callback(null, response);
            }

        });

    } else {
        const response = {
            headers: {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*" // Required for CORS support to work
            },
            statusCode: 403,
            body: JSON.stringify("UnAuthenticated"),
        };
        callback(null, response);
    }
}