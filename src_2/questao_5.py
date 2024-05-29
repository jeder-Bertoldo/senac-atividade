def converte_hora(hora, minuto):
    periodo = "A.M." if hora < 12 else "P.M."
    hora_12 = hora % 12
    if hora_12 == 0:
        hora_12 = 12
    return f"{hora_12}:{minuto:02d} {periodo}"

# Teste
hora = int(input("Informe a hora (0-23): "))
minuto = int(input("Informe o minuto (0-59): "))
print("Hora convertida:", converte_hora(hora, minuto))
