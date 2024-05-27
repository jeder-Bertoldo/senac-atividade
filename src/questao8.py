try:
    real = float(input("Informe a quantia em reais: "))
    taxa_dolar = float(input("Informe quantos reais vale um dólar: "))
    taxa_euro = float(input("Informe quantos reais vale um euro: "))

    dolares = real / taxa_dolar
    euros = real / taxa_euro

    print(f"{real} reais equivalem a {dolares:.2f} dólares e {euros:.2f} euros.")
except ValueError:
    print("Por favor, insira um valor numérico válido.")

