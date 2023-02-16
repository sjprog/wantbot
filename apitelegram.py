
# Nome do robo: WantBot  Want_SK_Bot

import time

import requests

import token_1

url_base = f'http://api.telegram.org/bot{token_1}'


while True:
    r = requests.get(url_base + "/getUpdates")

    resposta_dict = r.json()

    print(resposta_dict)

    time.sleep(5)
