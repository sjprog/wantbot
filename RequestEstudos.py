import requests

resp = requests.get("https://viacep.com.br/ws/01001000/json/")

# print(resp.text)

dd = resp.json()

dt = resp.text

print(dd)

