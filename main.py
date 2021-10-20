import requests
import time
import calendar


# get symbol name from the user
print("Please enter symbol name:")
symbol = input()

gmt = time.gmtime()
date = calendar.timegm(gmt)

# url of data for a particular stock
url = f"https://rest.yahoofinanceapi.com/v7/finance/options/{symbol}"

# query parameters
query_string = {
    "date": date
}

# our api-key
headers = {
    'x-api-key': "hNcYRonIR289365RnQK21aYvNCZ2cHL1aITV9jKB"
}

# request to the api
response = requests.request("GET", url, headers=headers, params=query_string)

try:
    data = response.json()
    quote = data["optionChain"]["result"][0]["quote"]
    closing_price = quote["regularMarketPreviousClose"]
    print(closing_price)
except Exception as e:
    print(str(e))
