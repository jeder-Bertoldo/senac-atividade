def reverso_numero(numero):
    return int(str(numero)[::-1])

# Teste
numero = int(input("Informe um número inteiro: "))
print("Reverso do número:", reverso_numero(numero))
