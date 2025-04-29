import pprint
import requests

def get_request(url, params=None):
    """
    Função para fazer uma requisição GET
    :param url: URL para a requisição
    :param params: Parâmetros da requisição
    :return: Resposta da requisição
    """
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Erro: {err}")
        return None
    return response.json()

def get_estados():
    """
    Função para obter a lista de estados
    :return: Lista de estados
    """
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    data_estados = get_request(url, params={"view": "nivelado"}) or []
    return {estado["UF-id"]: estado["UF-nome"] for estado in data_estados}

def name_frequence(name):
    """Obtem um dictionario de frequencia de um nome por estado
    formato {id_estado: {nome: frequencia}}
    """
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    data_frequencia = get_request(url, params={"groupBy": "UF"}) or []
    return {int(data["localidade"]): data["res"][0]["proporcao"] for data in data_frequencia}

def main(name):
    dict_estados = get_estados()
    dict_frequencia = name_frequence(name)
    print(f"===== Frequência do nome {name} por estado =====")
    for id_estado, frequencia in sorted(dict_frequencia.items(), 
                                        key=lambda item: item[1],
                                        reverse=True):
        print(f"-> {dict_estados.get(id_estado, "Desconhecido")}: {frequencia}")
    
if __name__ == "__main__":
    main("Lucas")
    