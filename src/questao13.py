salario = float(input("Digite o salário: "))
cargo = int(input("Digite o código do cargo (101 - Gerente, 102 - Engenheiro, 103 - Técnico): "))

aumentos = {
    101: 0.10,
    102: 0.20,
    103: 0.30
}

percentual_aumento = aumentos.get(cargo, 0.40)
novo_salario = salario * (1 + percentual_aumento)

print(f"Salário antigo: R$ {salario:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
print(f"Diferença: R$ {novo_salario - salario:.2f}")
