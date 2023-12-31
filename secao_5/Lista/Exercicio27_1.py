codigo_numerico = int(input('Digite um código númerico de cinco algarismos: '))

a = codigo_numerico // 10000
b = codigo_numerico % 10000 // 1000
c = codigo_numerico % 1000 // 100
d = codigo_numerico % 100 // 10
e = codigo_numerico % 10

s = (6 * a) + (5 * b) + (4 * c) + (3 * d) + (2 * e) 
digito_verificador = s % 7

print(f'{s}')
print(f'{digito_verificador}')
