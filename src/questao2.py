import math

try:
    a = float(input("Informe o coeficiente a (não zero): "))
    b = float(input("Informe o coeficiente b: "))
    c = float(input("Informe o coeficiente c: "))
    if a == 0:
        raise ValueError("O coeficiente a não pode ser zero.")
    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError("A equação não possui raízes reais.")
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são x1 =", x1, "e x2 =", x2)
except ValueError as e:
    print("Erro:", e)
