def data_por_extenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    dia, mes, ano = map(int, data.split('/'))
    if 1 <= dia <= 31 and 1 <= mes <= 12:
        return f"{dia} de {meses[mes-1]} de {ano}"
    else:
        return "NULL"

# Teste
data = input("Informe uma data (DD/MM/AAAA): ")
print("Data por extenso:", data_por_extenso(data))
