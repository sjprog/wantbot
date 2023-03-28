import json
import time

import requests

from token_1 import token


class TelegramBot:

    def __init__(self):
        self.url_base = f'http://api.telegram.org/bot{token}/'

    def Iniciar(self):
        find_cep = False

        updates = self.obter_updates()
        dados = updates["result"]
        chat_id_ = dados[-1]["message"]["from"]["id"]
        self.responder("Digite o CEP para encontrar o endereço.",chat_id_)

       
        while True:
            updates = self.obter_updates()            

            dados = updates["result"]

            # print(dados)
            pdate_id = dados[-1]['update_id']

            mensagem = str(dados[-1]["message"]["text"])
            chat_id_ = dados[-1]["message"]["from"]["id"]

            nome = dados[-1]["message"]["from"]["first_name"]

            if mensagem and not(find_cep):
                print("Aguardando cep...")
                if len(mensagem)==8:
                    print("Tamanho de cep Ok!")
                    c = self.get_info_cep(mensagem)
                    self.responder("Sua rua é = "+c['logradouro'],chat_id_)
                    self.responder("Seu estado é = "+c['uf'],chat_id_)
                    find_cep = True

            # print("Chat ID = ", chat_id_)
            # print('Mensagem = ', mensagem)

            # self.responder("Olá "+nome+" Meu nome é Robô Telegram. ",chat_id_)
            print("------------------------------")

            time.sleep(5)

    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


    def obter_updates(self):

        link_api = self.url_base + "getUpdates"

        r = requests.get(link_api)
        return r.json()
    
    def get_info_cep(self, cep):
        url_base = f'https://viacep.com.br/ws/{cep}/json/'
        r = requests.get(url_base)
        return r.json()
       

t = TelegramBot()
t.Iniciar()