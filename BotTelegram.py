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
            update_id = dados[-1]['update_id']

            mensagem = str(dados[0]["message"]["text"])
            chat_id_ = dados[-1]["message"]["from"]["id"]

            nome = dados[-1]["message"]["from"]["first_name"]

            print("Chat ID = ", chat_id_)
            print('Mensagem = ', mensagem)

            self.responder("Olá "+nome+" Meu nome é Robô Telegram. ",chat_id_)
            print("------------------------------")

            time.sleep(5)

    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


    def obter_updates(self):

        link_api = self.url_base + "getUpdates"

        r = requests.get(link_api)
        return r.json()
       

t = TelegramBot()
t.Iniciar()