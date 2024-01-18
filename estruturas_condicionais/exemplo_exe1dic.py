conceito = input('Digite um conceito entre A e E: ')
nota = 0.0
conceito_dic = {'A': 95.0, 'B': 85.0, 'C': 75.0, 'D': 65.0, 'E': 30.0}
nota = conceito_dic[conceito]

# if que testa se o conceito foi válido
if nota > 0.0:
    print(f'Conceito: {conceito} Nota: {nota}')
else:
    print(f'Conceito Inválido')

