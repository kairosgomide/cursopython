
maior_media = 0.0
maior_aluno = ''
for n in range(1, 4):
    aluno = input('Nome: ')
    notas = []
    for i in range(1, 6):
        notas.append(float(input(f'N{i}: ')))
    media = sum(notas) / len(notas)
    if media >= maior_media:
        maior_media = media
        maior_aluno = aluno
    print(f'Média: {media}')

print(f'Aluno com maior nota: {maior_aluno}')



