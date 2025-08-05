import random
import string

def gerar_senha(tamanho: int) -> str:
    if tamanho <= 0:
        return "Tamanho inválido."

    # Conjunto de caracteres: letras, dígitos e caracteres especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gerar senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Programa principal
try:
    tamanho = int(input("Informe o número de caracteres da senha: "))
    senha_gerada = gerar_senha(tamanho)
    print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
