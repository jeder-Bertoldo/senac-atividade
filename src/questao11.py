try:
    custo_fabrica = float(input("Informe o custo de fábrica do carro: "))

    percentual_distribuidor = 0.28
    impostos = 0.45

    custo_consumidor = custo_fabrica + (custo_fabrica * percentual_distribuidor) + (custo_fabrica * impostos)
    print(f"O custo ao consumidor do carro é de {custo_consumidor:.2f} reais.")
except ValueError:
    print("Por favor, insira um valor numérico válido.")
