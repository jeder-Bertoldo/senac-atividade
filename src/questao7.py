try:
    numero = int(input("Informe um número inteiro: "))
    divisivel = []
    if numero % 2 == 0:
        divisivel.append("2")
    if numero % 3 == 0:
        divisivel.append("3")
    if numero % 5 == 0:
        divisivel.append("5")
    if divisivel:
        print("O número é divisível por " + ", ".join(divisivel))
    else:
        print("O número não é divisível por 2, 3 ou 5")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
