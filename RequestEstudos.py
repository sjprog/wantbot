import requests

# resp = requests.get("https://viacep.com.br/ws/01001000/json/")

# # print(resp.text)

# dd = resp.json()

# dt = resp.text

# print(dd)


def get_info_cep(cep):

    url_base = f'https://viacep.com.br/ws/{cep}/json/'
    r = requests.get(url_base)
    return r.json()

d = get_info_cep('71825115')

# print(d)


def retorna_rua(d):
    return d['logradouro']


print(retorna_rua(d))