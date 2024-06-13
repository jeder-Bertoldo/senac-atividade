class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total_estoque(self):
        return self.preco * self.quantidade

    def esta_disponivel(self):
        return self.quantidade > 0

# Exemplo de uso
produto = Produto("Caneta", 1.50, 100)
print("Valor total em estoque:", produto.valor_total_estoque())
print("Produto disponível?", produto.esta_disponivel())
