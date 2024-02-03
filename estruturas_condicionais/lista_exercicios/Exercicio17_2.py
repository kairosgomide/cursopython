saldo_medio = int(input('Informe o seu saldo médio: '))

if saldo_medio >= 0 and saldo_medio <= 500:
    print(f'Saldo Médio: {saldo_medio}, Valor de crédito: Nenhum.')
elif saldo_medio > 500 and saldo_medio <= 1000:
    valor_credito = (30 * saldo_medio) / 100
    print(f'Saldo Médio: {saldo_medio}, Valor de crédito: {valor_credito}.')
elif saldo_medio >= 1001 and saldo_medio <= 3000:
    valor_credito = (40 * saldo_medio) / 100
    print(f'Saldo Médio: {saldo_medio}, Valor de crédito: {valor_credito}.')
else: 
    valor_credito = (50 * saldo_medio) / 100
    print(f'Saldo Médio: {saldo_medio}, Valor de crédito: {valor_credito}.')