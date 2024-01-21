valor_a = int(input('Escreva um valor para A: '))
valor_b = int(input('Escreva um valor para B: '))
valor_c = int(input('Escreva um valor para C: '))

if valor_a > valor_b and valor_a > valor_c and valor_b > valor_c:
    print(f'Em ordem decrescente é: {valor_a}, {valor_b}, {valor_c}')
elif valor_a > valor_b and valor_a > valor_c and valor_c > valor_b:
    print(f'Em ordem decrescente é: {valor_b}, {valor_c}, {valor_c}')
elif valor_b > valor_a and valor_b > valor_c and valor_c > valor_a:
    print(f'Em ordem decrescente é: {valor_b}, {valor_c}, {valor_a}')
elif valor_b > valor_a and valor_b > valor_c and valor_a > valor_c:
    print(f'Em ordem decrescente é: {valor_b}, {valor_a}, {valor_c}')
elif valor_c > valor_a and valor_c > valor_b and valor_b > valor_a:
    print(f'Em ordem decrescente é: {valor_c}, {valor_b}, {valor_a}')
elif valor_c > valor_a and valor_c > valor_b and valor_a > valor_b:
    print(f'Em ordem decrescente é: {valor_c}, {valor_a}, {valor_b}')