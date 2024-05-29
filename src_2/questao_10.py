import random

def embaralha_string(s):
    s = s.lower()  # Padronizando para caixa baixa
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)

# Teste
string = input("Informe uma string: ")
print("String embaralhada:", embaralha_string(string))
