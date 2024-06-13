class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor

    def exibir_saldo(self):
        print(f"Saldo da conta {self.numero} ({self.titular}): {self.saldo}")

# Exemplo de uso
conta = ContaBancaria(1234, "Alice", 1000)
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()
