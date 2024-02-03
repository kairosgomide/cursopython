import math

numero = float(input('Digite um número: '))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(raiz_quadrada)
elif numero < 0:
    quadrado = numero ** 2
    #math.pow(numero, 2)
    print(quadrado)
