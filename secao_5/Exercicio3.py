'''
A) Crie um dicionário chamado games
B) Crie duas chaves: 'melhores' e 'piores', os valores das chaves deverão ser listas vazias
C) Acesse a chave 'melhores' e adicione os 5 melhores jogos
D) Acesse a chave 'piores' e adicione os 5 piores jogos
E) Imprima a lista dos melhores jogos
F) Imprima a lista dos piores jogos
G) Imprima se na lista dos melhores jogos tem Minecraft (True ou False) - in
H) Imprima se na lista dos piores jogos não tem Roblox (True ou False) - not in
I) Remova um jogo da lista dos piores jogos
J) Imprima a lista dos piores jogos
'''

games = {'melhores': [], 'piores': []}
games['melhores'] = ['Elden Ring', 'Rocket League', 'Marvel Spider-man 2', 'BloodBorne', 'Overcooked 2']

games['piores'].append('Sea of Thieves')
games['piores'].append('Roblox')
games['piores'].append('Fortnite')
games['piores'].append('Call of Duty')
games['piores'].append('Limbo')

print(games['melhores'])
print(games['piores'])

print(f"Tem Minecraft? {'Minecraft' in games['melhores']}")
print(f"Não tem Roblox? {'Roblox' not in games['piores']}")

games['piores'].remove('Limbo')
print(games['piores'])


