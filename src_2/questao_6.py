def valor_pagamento(valor, dias_atraso):
    if dias_atraso == 0:
        return valor
    else:
        multa = valor * 0.03
        juros = valor * 0.001 * dias_atraso
        return valor + multa + juros

# Programa principal
total_prestacoes = 0
quantidade_prestacoes = 0

while True:
    valor = float(input("Informe o valor da prestação (0 para sair): "))
    if valor == 0:
        break
    dias_atraso = int(input("Informe os dias de atraso: "))
    valor_a_pagar = valor_pagamento(valor, dias_atraso)
    print("Valor a ser pago:", valor_a_pagar)
    total_prestacoes += valor_a_pagar
    quantidade_prestacoes += 1

print("Relatório do dia:")
print("Quantidade de prestações pagas:", quantidade_prestacoes)
print("Valor total das prestações pagas:", total_prestacoes)
