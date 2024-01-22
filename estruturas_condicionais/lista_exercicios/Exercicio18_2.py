idade = int(input('Digite a sua idade: '))

if idade < 18:
    print(f'Menor de idade.')
elif idade >= 18 and idade <= 64:
    print(f'Maior de idade.')
else:
    print(f'Pessoa idosa.')

