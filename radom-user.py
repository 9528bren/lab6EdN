import requests

def gerar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Gera erro para status HTTP >= 400

        dados = resposta.json()
        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("=== Perfil Gerado ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.RequestException as e:
        print(f"Erro ao conectar à API: {e}")
    except KeyError:
        print("Erro ao processar os dados recebidos.")

# Executa o programa
gerar_usuario_aleatorio()
