'''
A) Crie uma lista chamada meses
B) Adicione na lista todos os meses do ano
C) Imprima a lista
D) Inverta a seleção
E) Imprima a lista
F) Retire da lista os meses de Julho e Dezembro
G) Imprima a lista
H) Mostre a quantidade de elementos da lista
I) Imprima os elementos dos índices 2 e 4
'''

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print(meses)
meses.reverse()
print(meses)
meses.remove('Julho')
meses.remove('Dezembro')
print(meses)
print(len(meses))
print(f'{meses[2]} {meses[4]}')

