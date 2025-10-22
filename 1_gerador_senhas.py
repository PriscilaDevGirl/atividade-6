import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    tamanho = int(input("Digite o tamanho da senha: "))
    if tamanho < 4:
        print("A senha deve ter pelo menos 4 caracteres.")
    else:
        senha = gerar_senha(tamanho)
        print(f"Sua senha gerada é: {senha}")
except ValueError:
    print("Por favor, digite um número válido para o tamanho da senha.")
