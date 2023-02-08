# Primeira sprint

print('Ola Atenção!')

lista = ['Ricardo', 'Sidney', 'Kele', 'Lucas']

familia = {'Pai':'Sidney','Mãe':'Kele','TemFilhos':False}

familia2 = dict(Pai='Carlos',Mae='Cristina',TemFilhos=True)

lista_tuplas = [('pai','Joao',('Mae','maria'),('TemFilhos',False))]

print(familia2['Pai'])
familia2.values()


class Veiculo:
    def __init__(self,nome,tipo):
        self._nome = nome
        self. tipo = tipo
    
    def tipoVeiculo(self):
        print(self._nome)

v2 = Veiculo('Caminhao','Terrestre')

v2.tipoVeiculo()

moto = Veiculo("Honda","Terrestre")

barco = Veiculo("Barco pequeno","Maritimo")


import json

json_string = '{"primeiro_nome":"Sidney", "Ultimo_nome":"Siqueira"}'

json_dict = json.loads(json_string)

d = {
    'primeiro_nome': 'Sidney',
    'Segundo_nome': 'Siqueira',
    'Titles': ['BDFL', 'Developer'],
}

d_json = json.dumps(d)








