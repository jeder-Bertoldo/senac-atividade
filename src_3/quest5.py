class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = self.calcular_media()
        return "Aprovado" if media >= 6 else "Reprovado"

# Exemplo de uso
aluno = Aluno("João", "12345", [7, 8, 6])
print("Média do aluno:", aluno.calcular_media())
print("Situação do aluno:", aluno.verificar_situacao())
