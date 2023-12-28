valor_a = int(input('Escreva um número para A é '))
valor_b = int(input('Escreva um número para B é '))

print(f'O valor de A é {valor_a}')
print(f'O valor de B é {valor_b}')

valor_antigo_a = valor_a

valor_a = valor_b
valor_b = valor_antigo_a

print(f'invertendo os valores A é {valor_a}')
print(f'invertendo os valores B é {valor_b}')