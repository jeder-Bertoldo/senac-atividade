#Escreva um algoritmo em Python que leia um valor inteiro entre 1 e 12 e escreva
#por extenso o nome do mês correspondente ao número (obs. Não aceite
#números que não estejam nessa faixa de valores).

def nome_do_mes(numero):
    meses = {
        1: "janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
        }
    return meses.get(numero,"Numero invalido.")

while True:
    try:
        numero = int(input("Digite um numero entre 1 e 12: "))

        if 1 <= numero <= 12:
            print(f"O mês correspondente é {nome_do_mes(numero)}.")
            break
        else:
            print("Numero invalido. digite um numero entre 1 e 12.")
    except ValueError:
        print("entrada invalida. insira um numero inteiro")
