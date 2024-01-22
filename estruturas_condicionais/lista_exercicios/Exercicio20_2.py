lado_1 = int(input('Digite um valor para um lado de um triândulo: '))
lado_2 = int(input('Digite outro: '))
lado_3 = int(input('Mais um: '))

if lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
    print(f'Esse triângulo é escaleno.')
elif lado_1 == lado_2 and lado_1 == lado_3 and lado_2 == lado_3:
    print(f'Esse triângulo é equilatero.')
else:
    print(f'Esse triângulo é isosceles.')
