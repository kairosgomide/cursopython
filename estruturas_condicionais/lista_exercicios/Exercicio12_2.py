valor_a = int(input('Escreva um valor para A: '))
valor_b = int(input('Escreva um valor para B: '))
valor_c = int(input('Escreva um valor para C: '))
valor_d = int(input('Escreva um valor para D: '))

if valor_a > valor_b and valor_a > valor_c and valor_a > valor_d:
    print(f'{valor_a} é o maior entre eles')
elif valor_b > valor_a and valor_b > valor_c and valor_b > valor_d:
    print(f'{valor_b} é o maior entre eles')
elif valor_c > valor_a and valor_c > valor_b and valor_c > valor_d:
    print(f'{valor_c} é o maior entre eles')
elif valor_d > valor_a and valor_d > valor_b and valor_d > valor_c:
    print(f'{valor_d} é o maior entre eles')