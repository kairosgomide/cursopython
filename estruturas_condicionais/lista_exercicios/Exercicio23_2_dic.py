tabela = {
    'NORTE': (500, 900),
    'NORDESTE': (350, 650),
    'CENTRO-OESTE': (350, 600),
    'SUL': (300, 550)
}

regiao = input('Escolha uma região: NORTE, NORDESTE, CENTRO-OESTE, SUL => ').upper()
condicao = int(input('Digite: 0 - IDA e 1 - IDA e VOLTA => '))

print(tabela[regiao][condicao])