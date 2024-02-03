import random

a = int(input('Digite a: '))
b = int(input('Digite b: '))

lista = []

# range - ela gera um intervalo de n1 a n2
for n in range(1, 101):
    # randint - gera um valor aleatório entre a e b
    x = random.randint(a, b)
    lista.append(x)

print(lista)




'''
for n in range(1, 101):


i = 1
while i <= 100:
    ...
    i += 1
'''