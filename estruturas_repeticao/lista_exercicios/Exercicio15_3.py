n = int(input('Digite um número para ver se ele é primo ou não: '))
lista = []
primo = True

for i in range(1, (n**0.5) + 1):
        print(i)
        if n % i == 0:
                primo = False
        else:
                lista.append(i)
print(lista)
print(f'A soma de todos eles é: {sum(lista)}')