
lista = []
for n in range(1, 16):
    x = int(input('Digite qualquer número 15 vezes: '))
    if x > 30:
        lista.append(x)

print(lista)
print(f'Entre desses números que você escreveu tem {len(lista)} acima de 30')