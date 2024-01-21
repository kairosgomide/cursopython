numero = int(input('Digite um numero qualquer: '))

if numero % 3 == 0 and numero % 7 == 0:
    print(f'Esse número é divisível por 3 e 7')
elif numero % 3 == 0:
    print(f'Esse número é divisível por 3')
elif numero % 7 == 0:
    print(f'Esse número é divisível por 7')
else:
    print(f'Esse número não é divisível por 3 e 7')