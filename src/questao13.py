try:
    salario = float(input("Informe o salário do funcionário: "))
    codigo = int(input("Informe o código do cargo: "))

    aumentos = {101: 0.10, 102: 0.20, 103: 0.30}
    aumento = aumentos.get(codigo, 0.40)

    novo_salario = salario * (1 + aumento)
    diferenca = novo_salario - salario

    print(f"Salário antigo: {salario:.2f}")
    print(f"Novo salário: {novo_salario:.2f}")
    print(f"Diferença: {diferenca:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
