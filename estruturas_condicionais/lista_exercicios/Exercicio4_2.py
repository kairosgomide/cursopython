numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

soma = numero1 + numero2

if soma > 20:
    print(f'{soma + 8}')
elif soma <= 20:
    print(f'{soma - 5}')