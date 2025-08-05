import requests

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()

        if "erro" in dados:
            print("❌ CEP não encontrado.")
        else:
            print("=== Endereço encontrado ===")
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")

    except requests.RequestException as e:
        print(f"Erro na conexão: {e}")
    except ValueError:
        print("Erro ao processar a resposta da API.")

# Programa principal
cep_usuario = input("Digite o CEP (apenas números): ").strip()

# Verificação simples do formato
if len(cep_usuario) == 8 and cep_usuario.isdigit():
    consultar_cep(cep_usuario)
else:
    print("❌ CEP inválido. Digite exatamente 8 números.")
