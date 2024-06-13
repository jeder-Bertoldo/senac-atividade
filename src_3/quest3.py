class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

# Exemplo de uso
retangulo = Retangulo(5, 10)
print("Área do retângulo:", retangulo.calcular_area())
print("Perímetro do retângulo:", retangulo.calcular_perimetro())
