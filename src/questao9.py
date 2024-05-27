try:
    capital = float(input("Informe o capital em reais: "))
    meses = int(input("Informe o número de meses: "))
    taxa = 0.006  # 0.6% ao mês

    montante = capital * ((1 + taxa) ** meses)
    print(f"O valor com juros após {meses} meses é de {montante:.2f} reais.")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")

