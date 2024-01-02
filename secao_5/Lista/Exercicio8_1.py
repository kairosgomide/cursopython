print('Precisamos encontrar o valor de X e Y, então escreva um valor para cada letra')

a = float(input('Escreva o valor de A: '))
b = float(input('Escreva o valor de B: '))
c = float(input('Escreva o valor de C: '))
d = float(input('Escreva o valor de D: '))
e = float(input('Escreva o valor de E: '))
f = float(input('Escreva o valor de F: '))

x = (c * e - b * f) / (a * e - b * d)

y = (a * f - c * d) / (a * e - b * d)

print(f'Os valores de X e Y são aproximadamente, {x} e {y}, respectivamente')
