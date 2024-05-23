#volume do cone
import math

raio = int(input("Digite o raio do cone: "))
altura = int(input("Digite o raio do altura: "))

pi = 3.14

volume = (math.pi * raio **2)  * altura /3

volume_aredondado = round(volume, 2)

print("O volume do cone é ", volume_aredondado)