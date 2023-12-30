#Informações
salario_bruto = int(input('Digite o salário bruto de um cidadão: '))

#Cálculos
total_desconto = (15/100) * salario_bruto
salario_liquido = salario_bruto - total_desconto

#Resultados
print(f'O salário líquido é {salario_liquido}')