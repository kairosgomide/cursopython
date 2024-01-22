idade = int(input('Digite a sua idade: '))

if idade >= 5 and idade <= 7:
    print(f'Infantil A')
elif idade >= 8 and idade <= 10:
    print(f'Infantil B')
elif idade >= 11 and idade <= 13:
    print(f'Juvenil A')
elif idade >= 14 and idade <= 17:
    print(f'Juvenil B')
else:
    print(f'Sênior')
