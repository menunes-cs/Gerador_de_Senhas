import secrets
import string 
caracteres = string.ascii_letters + string.digits

tamanho = 8
senha = "".join(secrets.choice(caracteres) for _ in range(tamanho))
print(senha)