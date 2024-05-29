def quantidade_digitos(numero):
    return len(str(abs(numero)))

# Teste
numero = int(input("Informe um número inteiro: "))
print("Quantidade de dígitos:", quantidade_digitos(numero))
