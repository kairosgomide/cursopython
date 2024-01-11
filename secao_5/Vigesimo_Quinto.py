#5.51 Dicionário

pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
print(type(pessoa))
print(len(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][0])
print(pessoa['cursos'][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))

print(pessoa.get('tags', False))