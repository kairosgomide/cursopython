n = int(input('Digite um número: '))

lista = [1, 1]
for x in range(1, n+1):
        soma = lista[0] + lista[1]
        lista.append(soma)
        lista = sorted(lista, reverse=True)

print(sorted(lista, reverse=False))
