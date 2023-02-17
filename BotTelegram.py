import json
import time

import requests

from token_1 import token


class TelegramBot:

    def __init__(self):
        self.url_base = f'http://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            updates = self.obter_updates()

            dados = updates["result"]

            print(dados)
            update_id = dados[0]['update_id']
            print("Update ID = ", update_id)
            

            print("------------------------------")
            time.sleep(5)

    def obter_updates(self):

        link_api = self.url_base + "getUpdates"

        r = requests.get(link_api)
        return r.json()
       

