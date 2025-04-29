import requests
import pprint

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
# params = {
#     "view": "nivelado"
# }
response = requests.get(url)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Erro: {err}")
    resultado = None
else:
    resultado = response.json()
    pprint.pprint(resultado)