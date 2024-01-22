numero = int(input('Digite um número de 1 a 7: '))

if numero == 1: 
    print('Domingo')
elif numero == 2:
    print('SEGUNDA-FEIRA')
elif numero == 3:
    print('TERÇA-FEIRA')
elif numero == 4:
    print('QUARTA-FEIRA')
elif numero == 5:
    print('QUINTA-FEIRA')
elif numero == 6:
    print('SEXTA-FEIRA')
elif numero == 7:
    print('SÁBADO')
else:
    print(f'Não existe um dia da semana com esse número.')
