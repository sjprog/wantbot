
# Nome do robo: WantBot  Want_SK_Bot

import time

import requests

token = '6170956894:AAHR1o4NtuD7syuKFcGUwMHYMM6jkU4VA2I'

url_base = f'http://api.telegram.org/bot{token}'


while True:
    r = requests.get(url_base + "/getUpdates")

    resposta_dict = r.json()

    print(resposta_dict)

    time.sleep(5)
