a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))

lista = []

if b > a:
    for n in range(a, b+1):
        if n % 2 == 0:
            lista.append(n)
        n += 1
elif a > b:
    for n in range(b, a+1):
        if n % 2 == 0:
            lista.append(n)
        n += 1
print(lista)
print(f'E a soma de todos eles é {sum(lista)}')