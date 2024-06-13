class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = 0

    def acelerar(self, incremento):
        self.velocidade_atual += incremento

    def frear(self, decremento):
        self.velocidade_atual = max(0, self.velocidade_atual - decremento)

    def exibir_velocidade(self):
        print(f"Velocidade atual do {self.marca} {self.modelo}: {self.velocidade_atual} km/h")

# Exemplo de uso
carro = Carro("Toyota", "Corolla")
carro.acelerar(50)
carro.exibir_velocidade()
carro.frear(20)
carro.exibir_velocidade()
