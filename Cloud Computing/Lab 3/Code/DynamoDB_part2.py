from boto3.dynamodb.conditions import Key

dynamoDB = boto3.resource("dynamodb")
table = dynamoDB.Table("Currency_UAH_Python")

response1 = table.query(KeyConditionExpression=Key("cc").eq("SEK"))
response2 = table.query(KeyConditionExpression=Key("cc").eq("CAD"))
response3 = table.query(KeyConditionExpression=Key("cc").eq("HUF") & Key("exchangedate").eq("10.05.2021"))

print(response1["Items"])
print(response2["Items"])
print(response3["Items"])

dynamoDB = boto3.resource("dynamodb")
table = dynamoDB.Table("Currency_UAH_Python")

response = table.delete_item(Key = {"cc": "HUF", "exchangedate": "10.05.2021"})