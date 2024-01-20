valor_a = float(input('Digite o valor de A: '))
valor_b = float(input('Digite o valor de B: '))

if valor_a > valor_b:
    print(f'{valor_a} é maior que {valor_b}')
elif valor_a < valor_b:
    print(f'{valor_b} é maior que {valor_a}')
elif valor_a == valor_b:
    print(f'{valor_a} é igual a {valor_b}')