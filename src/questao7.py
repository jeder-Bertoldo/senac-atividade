numero = int(input("Digite um número inteiro: "))
divisiveis = []
if numero % 5 == 0:
    divisiveis.append(5)
if numero % 3 == 0:
    divisiveis.append(3)
if numero % 2 == 0:
    divisiveis.append(2)

if divisiveis:
    print(f"O número {numero} é divisível por: {', '.join(map(str, divisiveis))}.")
else:
    print(f"O número {numero} não é divisível por 5, 3 ou 2.")
