import requests as request
import json
import pandas as pd

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

df = pd.read_json("request.json")

df1 = pd.read_json(r"request.json")
df1.to_csv (r"request.csv", index = None)

# print(df.head(6), "\n")

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json("request.json")

plt.figure(figsize=(14, 4.5))

def plot(currency,color):
    x = []
    y = []
    month = 1

    for i in df.index:
        cc = currency
        if (month < 10): date = "10.0" + str(month) + ".2021"
        else: date = "10." + str(month) + ".2021"
        
        if df.loc[i,"cc"] == cc and df.loc[i,"exchangedate"] == date:
            x.append(month)
            y.append(df.loc[i,"rate"])
            month = month + 1

    plt.grid()
    plt.title(currency + " to UAH")
    plt.plot(x,y,color=color)

plt.subplot(1,2,1)
plot("USD", "green")
plt.subplot(1,2,2)
plot("EUR", "blue")

plt.savefig("exchange_rate.png")
# plt.show()
