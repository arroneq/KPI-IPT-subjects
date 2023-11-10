import requests as request
import json

response = request.get(
    "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json" + "&date=20210110")
json_data = response.json()

for i in range(2,13):
    if (i < 10):
        response = request.get(
            "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json" + "&date=20210" + str(i) + "10")
        json_data = json_data + response.json()
    else:
        response = request.get(
            "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json" + "&date=2021" + str(i) + "10")
        json_data = json_data + response.json()

jsonString = json.dumps(json_data, ensure_ascii=False, indent = 4)
jsonFile = open("request.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

import pandas as pd

df = pd.read_json("request.json")
print(df.head(6), "\n")
print(df.tail(6))

df = pd.read_json (r"request.json")
df.to_csv (r"request.csv", index = None)

import boto3

s3 = boto3.client("s3")

obj = s3.get_object(Bucket="bucket01my", Key="request.csv") 

df_from_s3 = pd.read_csv(obj["Body"])
print(df_from_s3)

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 4.5))

def plotting(currency, color):
    x = []
    y = []
    month = 1

    for i in df_from_s3.index:
        cc = currency
        if (month < 10): date = "10.0" + str(month) + ".2021"
        else: date = "10." + str(month) + ".2021"
        
        if df_from_s3.loc[i,"cc"] == cc and df_from_s3.loc[i,"exchangedate"] == date:
            x.append(month)
            y.append(df_from_s3.loc[i,"rate"])
            month = month + 1
            
    plt.xlabel("Monthes")
    plt.ylabel("Values of " + currency)
    plt.grid()
    plt.title(currency + " to UAH")
    plt.plot(x,y,color=color)

plt.subplot(1,2,1)
plotting("USD", "green")
plt.subplot(1,2,2)
plotting("EUR", "blue")

plt.savefig("exchange_rate.png")
plt.show()