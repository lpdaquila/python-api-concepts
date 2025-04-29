import requests
import pprint

nome = input("Digite um nome para pesquisa:\n")
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
params = {
    "localidade": 33 #RJ
}
response = requests.get(url, params=params)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Erro: {err}")
    resultado = None
else:
    resultado = response.json()
    pprint.pprint(resultado[0]["res"])