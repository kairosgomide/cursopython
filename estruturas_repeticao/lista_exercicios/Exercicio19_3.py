n = int(input('Digite um número: '))
y = 3
z = 1
lista = [1, ]
for x in range(1, n+1):
        z = z + y
        lista.append(z)
        y = 2 + y

print(lista)
        