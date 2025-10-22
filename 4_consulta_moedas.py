import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, BTC): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    chave = f"{moeda}BRL"
    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        cotacao = dados[chave]
        print(f"Moeda: {cotacao['name']}")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Máxima: R$ {cotacao['high']}")
        print(f"Mínima: R$ {cotacao['low']}")
        print(f"Última atualização: {cotacao['create_date']}")

except requests.exceptions.RequestException:
    print("Falha ao conectar à API AwesomeAPI.")
