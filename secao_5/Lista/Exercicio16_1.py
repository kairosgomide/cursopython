#Informações
salario_bruto = int(input('Digite o salário bruto de um cidadão: '))

#Cálculos
descontoA = 0.10 * salario_bruto
descontoB = 0.05 * (salario_bruto - descontoA)

#Resultados
print(f'O salário líquido é {salario_bruto - descontoA - descontoB}')





