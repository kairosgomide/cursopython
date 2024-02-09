n = int(input('Digite um número: '))

lista = []
for i in range(2, n+2):
        h = 1 + (1 / i)
        lista.append(h)

print(f'{sum(lista)}')
