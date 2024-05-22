custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
percentual_distribuidor = 0.28
percentual_impostos = 0.45

custo_distribuidor = custo_fabrica * percentual_distribuidor
impostos = custo_fabrica * percentual_impostos
custo_consumidor = custo_fabrica + custo_distribuidor + impostos

print(f"O custo ao consumidor é: R$ {custo_consumidor:.2f}")
