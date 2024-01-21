numero = int(input('Digite um número: '))

if numero == 5:
    print('Esse numero é igual a 5')
elif numero == 200:
    print('Esse numero é igual a 200')
elif numero == 400:
    print('Esse numero é igual a 400')
elif numero >= 500 and numero <= 1000:
    print('Esse numero está entre 500 e 1000')
else:
    print('Esse número não é 5, 200, 400 e não está entre 500 e 1000')