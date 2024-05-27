try:
    numero = int(input("Informe um número entre 0 e 10: "))
    numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis",
               "sete", "oito", "nove", "dez"]
    if 0 <= numero <= 10:
        print("O número por extenso é", numeros[numero])
    else:
        raise ValueError("Número fora da faixa permitida.")
except ValueError as e:
    print("Erro:", e)
