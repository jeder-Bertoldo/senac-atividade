A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A % B == 0 or B % A == 0:
    print(f"{A} e {B} são múltiplos.")
else:
    print(f"{A} e {B} não são múltiplos.")
