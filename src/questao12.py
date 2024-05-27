try:
    A = int(input("Informe o valor de A: "))
    B = int(input("Informe o valor de B: "))

    if A % B == 0:
        print(f"{A} é múltiplo de {B}.")
    elif B % A == 0:
        print(f"{B} é múltiplo de {A}.")
    else:
        print(f"{A} e {B} não são múltiplos um do outro.")
except ValueError:
    print("Por favor, insira valores inteiros válidos.")
