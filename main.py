import random
import string

print("Gerador de Senhas")

caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

def gerar_senha():
    tamanho = int(input("Digite o tamanho da senha: "))
    embaralha = random.sample(caracteres, tamanho)
    senha = "".join(embaralha)

    print("Sua nova senha:" + senha)
    
print(gerar_senha())