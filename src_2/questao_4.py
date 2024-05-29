def soma_imposto(taxa_imposto, custo):
    custo_com_imposto = custo + (custo * taxa_imposto / 100)
    return custo_com_imposto

# Teste
taxa = float(input("Informe a taxa de imposto (%): "))
custo = float(input("Informe o custo do item: "))
print("Custo com imposto:", soma_imposto(taxa, custo))
