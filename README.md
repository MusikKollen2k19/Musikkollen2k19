# MusikKollen2k19

[musikkollen2k19.github.io](https://musikkollen2k19.github.io/)


## Ladda upp nuvarande sida

Se till att du har lagt till din ssh nyckel i github först.

Använd ./deploy.sh för att ladda upp den nuvarde sidan till den som finns online

### SSH nyklar

Detta vet du om du kör (i bash) `ssh git@github.com` och får tillbaka ditt användarnamn

Annars kör du `cat ~/.ssh/id_rsa.pub` och kopierar från ssh.rsa till innan ditt användarnamn

Gå in på [Github](https://github.com/settings/keys) > settings > SSH and GPG keys och följ instruktionerna


## Api Struktur

### URL

https://km1wzv5ri1.execute-api.us-east-1.amazonaws.com/v1

### GET - hämta alla skolors info

Ingen body.

Exempel på response body:

    [
        {
            "CurrentAmount": 110,
            "Ansvarig": "abb_person",
            "Skola": "ABB",
            "LastAmount": [
                100,
                10,
                10,
                -10
            ],
            "LastUpdate": [
                "2019-11-30 12:14:39.790517",
                "2019-11-30 12:14:53.311116",
                "2019-11-30 12:50:51.632377",
                "2019-11-30 12:53:19.241188"
            ]
        },
        {
            "CurrentAmount": -1119,
            "Ansvarig": "rudbeck_person",
            "Skola": "Rudbeck",
            "LastAmount": [
                -100,
                -10,
                -10,
                -999
            ],
            "LastUpdate": [
                "2019-11-30 12:14:39.790517",
                "2019-11-30 12:14:53.311116",
                "2019-11-30 12:50:51.632377",
                "2019-11-30 12:53:19.241188"
            ]
        }
    ]

### PUT - ladda upp ny data

Exempel body:

    {
      "user": "abb_person",
      "pass": "<SHA-256 hash av lösenord>",
      "Amount": 10
    }

Du kommer att få tillbaka antingen statuskod 200 eller 201 där 200 är bra och 201 är dålig.

Exempel på response body:

    {
        "Success": false,
        "Meddelande": "HIttade inte användaren!"
    }

Eller:

    {
        "Success": true,
        "Meddelande": "Uppdaterade Värdet!"
    }
