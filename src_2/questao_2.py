def imprime_sequencia(n):
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)

# Teste
n = int(input("Informe o valor de n: "))
imprime_sequencia(n)
