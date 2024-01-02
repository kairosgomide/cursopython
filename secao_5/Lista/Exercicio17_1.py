nome = input('Digite o seu nome: ')
salario_fixo = int(input('Digite o seu salário fixo: '))
vendas_efetuadas = int(input('Digite o total de vendas efetuadas no mês(em dinheiro): '))

comissao = 15 * vendas_efetuadas / 100

print(f'Comissão: {comissao}')
print(f'Nome: {nome}, salário fixo: R$ {salario_fixo}, salário com a comissão: R$ {salario_fixo + comissao}')