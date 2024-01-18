conceito = input('Digite um conceito entre A e E: ')
nota = 0.0

# if que converte um conceito para nota
if conceito == 'A':
    nota = 95.0
elif conceito == 'B':
    nota = 85.0
elif conceito == 'C':
    nota = 75.0
elif conceito == 'D':
    nota = 65.0
elif conceito == 'E':
    nota = 30.0


# if que testa se o conceito foi válido
if nota > 0.0:
    print(f'Conceito: {conceito} Nota: {nota}')
else:
    print(f'Conceito Inválido')

