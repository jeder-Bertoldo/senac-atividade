def numero_por_extenso(numero):
    numeros = [
        "zero", "um", "dois", "três", "quatro", 
        "cinco", "seis", "sete", "oito", "nove", "dez"
    ]
    if 0 <= numero <= 10:
        return numeros[numero]
    else:
        return "Número inválido. Por favor, insira um valor entre 0 e 10."

while True:
    try:
        numero = int(input("Digite um número entre 0 e 10: "))
        if 0 <= numero <= 10:
            print(f"O número {numero} por extenso é '{numero_por_extenso(numero)}'.")
            break
        else:
            print("Número inválido. Por favor, insira um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
