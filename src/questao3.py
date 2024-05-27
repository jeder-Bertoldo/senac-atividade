import math

try:
    r = float(input("Informe o raio do cone: "))
    h = float(input("Informe a altura do cone: "))
    if r < 0 or h < 0:
        raise ValueError("Raio e altura devem ser positivos.")
    volume = (math.pi * r**2 * h) / 3
    print("O volume do cone é", volume)
except ValueError as e:
    print("Erro:", e)
