import requests
import base64

url = "https://api.kroger.com/v1/connect/oauth2/token"
client_id = "brokeproject-1a2ec4a74d7582cd0cb0e591a56d529d5634222003217603174"
client_secret = "udUhZfJCHZMKROZdnz_qXzmiPkso5BGgiln33mfa"
scope = "product.compact"

headers = {
"Content-Type": "application/x-www-form-urlencoded",
"Authorization": f"Basic {base64.b64encode((client_id + ':' + client_secret).encode()).decode()}"
}

data = {
"grant_type": "client_credentials",
"scope": scope
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print(response.json())
else:
    print("Error occurred with status code: ", response.status_code)



url = "https://api.kroger.com/v1/products"



headers = {
    "Accept": "application/json",
    "Authorization": "Bearer https://api.kroger.com/v1/connect/oauth2/token"
}

product = "milk"

params = {
    "filter.term": product,
    # "filter.locationId": "{{LOCATION_ID}}"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print("Error occurred with status code: ", response.status_code)