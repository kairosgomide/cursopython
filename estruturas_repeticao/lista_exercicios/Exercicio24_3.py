
lista = {'sexo': '', 'altura':  }
for x in range(1, 5):
        altura = float(input('Digite a sua altura: '))
        codigo = input('Escreva "1" se for masculino e "2" para feminino: ')
        lista[sexo].append(codigo)
        lista[altura].append(altura)

lista = sorted(lista[altura], reverse=True)
print(f'maior da sala: {lista[altura][0]}, menor da sala: {lista[altura][3]}')


if lista[altura] == '2':
        media_das_mulheres = sum(lista[altura]) / 10
        print(media_das_mulheres)

media_total = sum(lista[altura]) / 10
print(media_total)
