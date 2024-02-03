import random

valores = []
for n in range(1, 101):
    #d = float(input('Digite a distância: '))
    #t = float(input('Digite o tempo: '))
    d = random.randint(40, 120)
    t = random.randint(1, 3)
    vm = d / t
    if vm >= 80:
        valores.append(vm)
    
print(f'Porcentagem de veículos que ultrapassaram 80 km/h: {len(valores)}%')

