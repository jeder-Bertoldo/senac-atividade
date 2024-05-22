import math

# Função 
def calcular_raizes(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        x = -b / (2 * a)
        return f"A equação possui uma raiz real: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"A equação possui duas raízes reais: x1 = {x1} e x2 = {x2}"

# Entrada
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Cálculo das raízes
resultado = calcular_raizes(a, b, c)
print(resultado)
