import requests

def consultar_cotacao(moeda: str):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave not in dados:
            print("❌ Moeda não encontrada. Verifique o código informado.")
            return

        info = dados[chave]

        print(f"=== Cotação {moeda}/BRL ===")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Valor máximo do dia: R$ {info['high']}")
        print(f"Valor mínimo do dia: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}")

    except requests.RequestException as e:
        print(f"Erro na conexão com a API: {e}")
    except ValueError:
        print("Erro ao processar os dados da API.")

# Programa principal
moeda_usuario = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip()

if moeda_usuario:
    consultar_cotacao(moeda_usuario)
else:
    print("❌ Código da moeda não pode estar vazio.")
