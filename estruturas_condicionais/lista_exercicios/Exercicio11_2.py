salario_bruto = int(input('Digite o salário: '))
valor_prestacao = int(input('Diga o valor da prestação: '))

calculo = (30 * salario_bruto) / 100
#calculo = 0.30 * salario_bruto

if calculo > valor_prestacao:
    print(f'O emprestimo pode ser concedido')
else:
    print(f'O emprestimo não pode ser concedido')


#(30 * 100) / 100