import math

raio_circunferencia = int(input(f'Dê uma valor ao raio de uma circunferência: '))

# area = (raio_circunferencia * raio_circunferencia) * 3.14159

area = (raio_circunferencia ** 2) * math.pi

print(f'Valor de pi {math.pi}')
print(f'A área dessa circunferência é {area} metros')
