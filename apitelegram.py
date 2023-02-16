import requests

url_telegram_base = "http://api.telegram.org/bot6170956894:AAHR1o4NtuD7syuKFcGUwMHYMM6jkU4VA2I"

resposta = requests.post(url_telegram_base + "/getUpdates")

resposta_dict = resposta.json()