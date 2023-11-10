import boto3
dynamoDB = boto3.resource("dynamodb")

table = dynamoDB.create_table(
    TableName = "Currency_UAH_Python",

        KeySchema = [
            {
                "AttributeName": "cc",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "exchangedate",
                "KeyType": "RANGE"
            }],

        AttributeDefinitions = [
            {
                "AttributeName": "cc",
                "AttributeType": "S"
            },
            {
                "AttributeName":"exchangedate",
                "AttributeType": "S"
            }],

        ProvisionedThroughput={
                "ReadCapacityUnits":10,
                "WriteCapacityUnits":5
            }
    )

table = dynamoDB.Table("Currency_UAH_Python")

response = table.put_item(
    Item = { 
        "r030": 124,
        "txt": "Канадський долар",
        "rate": "21.6966",
        "cc": "CAD",
        "exchangedate": "10.02.2021"
    }
)
response = table.put_item(
    Item = { 
        "r030": 348,
        "txt": "Форинт",
        "rate": "0.093238",
        "cc": "HUF",
        "exchangedate": "10.05.2021"
    }
)
response = table.put_item(
    Item = { 
        "r030": 203,
        "txt": "Чеська крона",
        "rate": "1.2539",
        "cc": "CZK",
        "exchangedate": "10.03.2021"
    }
)
response = table.put_item(
    Item = { 
        "r030": 752,
        "txt": "Шведська крона",
        "rate": "3.2561",
        "cc": "SEK",
        "exchangedate": "10.04.2021"
    }
)