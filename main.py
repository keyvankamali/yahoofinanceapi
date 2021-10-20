import requests
import time
import calendar


print("Please enter symbol name:")
symbol = input()

gmt = time.gmtime()
date = calendar.timegm(gmt)

url = f"https://rest.yahoofinanceapi.com/v7/finance/options/{symbol}"

query_string = {
    "date": date
}

headers = {
    'x-api-key': "hNcYRonIR289365RnQK21aYvNCZ2cHL1aITV9jKB"
}

response = requests.request("GET", url, headers=headers, params=query_string)


data = response.json()
quote = data["optionChain"]["result"][0]["quote"]
closing_price = quote["regularMarketPreviousClose"]
print(closing_price)
