import random

b = int(input('Escreva um número: '))
n = int(input('Escreva um número: '))
lista = []

for x in range(1, n):
    a = random.randint(b, n)
    lista.append(a)

print(lista)
print(f'O maior entre eles é {max(lista)}')