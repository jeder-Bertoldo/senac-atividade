try:
    a = float(input("Informe o coeficiente a (não zero): "))
    b = float(input("Informe o coeficiente b: "))
    if a == 0:
        raise ValueError("O coeficiente a não pode ser zero.")
    x = -b / a
    print("A solução da equação é x =", x)
except ValueError as e:
    print("Erro:", e)

