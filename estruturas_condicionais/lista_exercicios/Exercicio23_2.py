destino = input('Escreva o seu destino: ')
ida_volta = input('É ida e volta: ')

ida_volta = ida_volta.upper()

if destino == 'Região Norte' and  ida_volta == 'SIM':
    print(f'Preço da passagem: R$900,00')
elif destino == 'Região Norte' and  ida_volta == 'NAO':
    print(f'Preço da passagem: R$500,00')
elif destino == 'Região Nordeste' and  ida_volta == 'SIM':
    print(f'Preço da passagem: R$650,00')
elif destino == 'Região Nordeste' and  ida_volta == 'NAO':
    print(f'Preço da passagem: R$350,00')
elif destino == 'Região Centro-Oeste' and  ida_volta == 'SIM':
    print(f'Preço da passagem: R$600,00')
elif destino == 'Região Centro-Oeste' and  ida_volta == 'NAO':
    print(f'Preço da passagem: R$350,00')
elif destino == 'Região Sul' and  ida_volta == 'SIM':
    print(f'Preço da passagem: R$550,00')
elif destino == 'Região Sul' and  ida_volta == 'NAO':
    print(f'Preço da passagem: R$300,00')