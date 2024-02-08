lista = []

for x in range(1, 11):
    numero = int(input('Digite 10 números: '))
    lista.append(numero)

lista_decrescente = sorted(lista, reverse=True)
print(f'O maior entre eles é: {max(lista_decrescente)}, e o segundo maior é: {lista_decrescente[1]}')