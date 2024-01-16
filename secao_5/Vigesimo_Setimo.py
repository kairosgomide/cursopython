#5.53 Interpolação

from string import Template

nome, idade = 'Ana', 30.9875

print('Nome: %s, Idade: %d' % (nome, idade)) #Versão mais antiga
print('Nome: %s, Idade: %f' % (nome, idade))
print('Nome: %s, Idade: %.2f' % (nome, idade))

nome, idade = 'Ana', 30

print('Nome: {0}, Idade: {1}'.format(nome, idade)) #Python < 3.6

print(f'Nome: {nome}, Idade: {idade}') #Python >= 3.6

s = Template('Nome = $n, Idade: $i')
print(s.substitute(n=nome, i=idade))

