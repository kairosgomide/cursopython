numero = 5

if numero % 2 == 0:
    print(f'PAR')
else:
    print(f'IMPAR')

# Usado para um um if/else simples que possua apenas uma linha de comando
resultado = 'PAR' if numero % 2 == 0 else 'IMPAR'
print(f'{resultado}')


user = 'ADMIN'
password = '123'

if user == 'ADMIN' and password == '123':
    print('Seja bem-vindo')


numero1 = 0
if numero1 > 0:
    print(f'POSITIVO')
elif numero1 < 0:
    print(f'NEGATIVO')
else:
    print(f'ZERO')



