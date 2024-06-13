import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def e_valido(self):
        return (self.lado1 + self.lado2 > self.lado3) and (self.lado1 + self.lado3 > self.lado2) and (self.lado2 + self.lado3 > self.lado1)

    def calcular_area(self):
        if self.e_valido():
            s = (self.lado1 + self.lado2 + self.lado3) / 2
            return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        else:
            return "Não é um triângulo válido"

# Exemplo de uso
triangulo = Triangulo(3, 4, 5)
print("É um triângulo válido?", triangulo.e_valido())
print("Área do triângulo:", triangulo.calcular_area())
