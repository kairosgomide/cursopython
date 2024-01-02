#5.33 Operadores Lógicos

#True or False

#print(7 != 3 and 2 > 3) 

#Tabela Verdade do AND
'''
True and True = True
True and False = False
False and True = False
False and False = False
'''
#Tabela Verdade do OR
'''
True or True = True
False or True = True
True or False = True
False or False = False
'''
#Tabela Verdade do Xor
'''
True != True = False
True != False = True
False != True = True
False != False = False
'''
#Operador de Negação (unário)
'''
not True = False
not False = True
'''
#Cuidado!
'''
True & False
True | False
True ^ False
'''

saldo = 1000
salario = 4000
despesas = 2967

meta = (saldo > 0) and (salario - despesas >= 0.2 * salario)
print(meta)

# Digite o usuário e a senha de uma pessoa. E compare se ele pode fazer login. Ele só entra se o usuário for ADMIN e a senha for 123. Imprima o resultado na tela
print('programa 1:')

usuario = input('Escreva o seu usuário: ')
senha = input('Escreva a sua senha: ')

comparacao = usuario == 'ADMIN' and senha == '123'
print(comparacao)


# Digite se está fazendo sol (is_sun = SIM NAO) e se a pesso tem dinheiro (is_money = SIM NAO). O programa deverá imprimir se ele poderá ir ao shopping. Só poderá ir ao shopping
# se estiver fazendo sol ou se tiver dinheiro.
print('programa 2: ')

is_sun = input('Digite "SIM" ou "NAO" se está fazendo sol: ')
is_money = input ('Digite "SIM" ou "NAO" se você tem dinheiro: ')

condicao = is_money.upper() == "SIM" or is_sun.upper() == "SIM"
print(condicao)


