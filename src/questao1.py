
def resolver_equacao(a, b):

    if a == 0:
        if b == 0:
         print ("A equação é indeterminada: tem infinitas soluções.") 

        else:
            print("A equação é impossivel! não há soluções")
    else:
        x = -b / a
    print("O valor de X na equação é: ", x)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

print(resolver_equacao(a, b))

