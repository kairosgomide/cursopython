peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 20:
    print(f'ABAIXO DO PESO')
elif imc >= 20 and imc < 25:
    print(f'PESO NORMAL')
elif imc >= 25 and imc < 30:
    print(f'SOBRE PESO')
elif imc >= 30 and imc <= 40:
    print(f'OBESO')
elif imc > 40:
    print(f'OBESO MÓRBIDO')