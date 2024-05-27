try:
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
