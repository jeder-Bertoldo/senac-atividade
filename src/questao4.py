try:
    numero = int(input("Informe um número entre 1 e 12: "))
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if 1 <= numero <= 12:
        print("O mês é", meses[numero - 1])
    else:
        raise ValueError("Número fora da faixa permitida.")
except ValueError as e:
    print("Erro:", e)

