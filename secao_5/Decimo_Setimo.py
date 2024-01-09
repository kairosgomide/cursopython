#5.45 Tipo String
#aula 1

#print(dir(str))

nome = 'Saulo Pedro'
print(nome)
print(nome[0])
#print(nome[0] = 'P')

#print('marca d' água')
print("Dias D' Avila" == 'Dias D\' Avila')

texto = 'Texto entre \
apostrófos pode ter "aspas"'
print(texto)

print("teste \" funciona!")

doc = """texto com múltiplas
... linhas"""
print(doc)
print('Texto com multiplas\n... \tlinhas')

doc2 = '''Também é possivel
... com três aspas simples'''
print(doc2)