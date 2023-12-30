#Informações

ht = int(input('Digite as horas trabalhadas por mês: '))
vh = int(input('Digite o valor por hora trabalhada: '))
pd = int(input('Digite o porcentual de desconto: '))

#Cálculos

sb = ht * vh
td = (pd/100) * sb
sl = sb - td

print(f'Horas Trabalhadas: {ht}')
print(f'Salário Bruto: {sb}')
print(f'Total de Desconto: {td}')
print(f'Sálario Liquido: {sl}')