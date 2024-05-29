def imprime_sequencia_ate_n(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Teste
n = int(input("Informe o valor de n: "))
imprime_sequencia_ate_n(n)
