tabela = {'P': [], 'C': [], 'G': []}

caloria = 0.1

while caloria > 0:
    nome = input('Nome do produto: ')
    caloria = float(input('Calorias: '))
    categoria = input('Digite P - para proteina; C - para carboidrato ou G - para gordura: ')

    if caloria > 0:
        tabela[categoria].append(caloria)


print(tabela)
p = tabela['P']
c = tabela['C']
g = tabela['G']
print(f'P: {sum(p)}')
print(f'C: {sum(c)}')
print(f'G: {sum(g)}')

