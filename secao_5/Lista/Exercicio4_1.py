print('Escreva a sua idade em anos, meses e dias')

idade = int(input('anos: '))
idade_meses = int(input('meses: '))
idade_dias = int(input('dias: '))

total_dias = idade * 365 + idade_meses * 30 + idade_dias 

print(f'Você já viveu {total_dias}')