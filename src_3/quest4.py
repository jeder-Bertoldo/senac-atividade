class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_salario_liquido(self):
        impostos = self.salario * 0.2
        beneficios = self.salario * 0.1
        return self.salario - impostos + beneficios

# Exemplo de uso
funcionario = Funcionario("Maria", 5000, "Gerente")
print("Salário líquido:", funcionario.calcular_salario_liquido())
