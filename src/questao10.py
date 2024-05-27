try:
    A = int(input("Informe o valor de A: "))
    B = int(input("Informe o valor de B: "))
    C = int(input("Informe o valor de C: "))

    if A < 0 or B < 0 or C < 0:
        raise ValueError("Os números devem ser inteiros e positivos.")

    R = (A + B) ** 2
    S = (B + C) ** 2
    D = (R + S) / 2

    print(f"O valor de D é {D:.2f}.")
except ValueError as e:
    print("Erro:", e)
