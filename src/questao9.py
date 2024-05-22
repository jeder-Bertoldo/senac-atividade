valor = float(input("Digite a quantia em reais: "))
meses = int(input("Digite o número de meses: "))
taxa = 0.006

valor_futuro = valor * ((1 + taxa) ** meses)
print(f"O valor após {meses} meses com juros compostos de 0,6% ao mês será de R$ {valor_futuro:.2f}.")
