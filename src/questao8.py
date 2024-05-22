reais = float(input("Digite a quantia em reais: "))
valor_dolar = float(input("Digite o valor de um dólar em reais: "))
valor_euro = float(input("Digite o valor de um euro em reais: "))

dolares = reais / valor_dolar
euros = reais / valor_euro

print(f"{reais} reais equivalem a {dolares:.2f} dólares.")
print(f"{reais} reais equivalem a {euros:.2f} euros.")
