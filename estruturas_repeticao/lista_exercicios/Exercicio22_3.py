n = int(input('Digite um número: '))
z = n

lista = [(n - 1) / 2 + n, ]
for i in range(1, n+1):
        s = i / z
        lista.append(s)
        z = n - i

print(lista)
print(f'{sum(lista)}')
