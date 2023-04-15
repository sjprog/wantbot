
# Nome do Rob: WantBot  Want_SK_Bot

import time

import requests

from token_1 import token_s

url_base = f'http://api.telegram.org/bot{token_s}'


while True:
    r = requests.get(url_base + "/getUpdates")

    resposta_dict = r.json()

    # print(resposta_dict)
    print(resposta_dict['result'])

    time.sleep(5)



    
