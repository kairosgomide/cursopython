import random

jogadas = [0, 0, 0, 0, 0, 0]
for n in range(1, 2501):
    randomico = random.randint(0, 5)
    #jogadas[randomico] = jogadas[randomico] + 1
    jogadas[randomico] += 1

for n in jogadas:
    p = n / 25
    print(f'{p}%')


'''
p1 = jogadas[0] / 25
p2 = jogadas[1] / 25
p3 = jogadas[2] / 25
p4 = jogadas[3] / 25
p5 = jogadas[4] / 25
p6 = jogadas[5] / 25
print(f'{p1}% {p2}% {p3}% {p4}% {p5}% {p6}%')
'''