n = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))
lista = [y, z]
for x in range(1, n+1):
        soma = lista[0] + lista[1]
        lista.append(soma)
        lista = sorted(lista, reverse=True)

print(sorted(lista, reverse=False))
print(f'{sum(lista)}')