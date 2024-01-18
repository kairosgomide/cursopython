massa = float(input('Digite o seu peso: '))
planeta = int(input('Digite o número do planeta: '))

print(f'Seu peso no planeta Terra: {massa}')

if planeta == 1:
    peso = massa * 0.37
    print(f'Seu peso em Mercúrio é: {peso}') 
elif planeta == 2:
    peso = massa * 0.88
    print(f'Seu peso em Vênus é: {peso}') 
elif planeta == 3:
    peso = massa * 0.38
    print(f'Seu peso em Marte é: {peso}')  
elif planeta == 4:
    peso = massa * 2.64
    print(f'Seu peso em Jupiter é: {peso}')  
elif planeta == 5:
    peso = massa * 1.15
    print(f'Seu peso em Saturno é: {peso}')  
elif planeta == 6:
    peso = massa * 1.17
    print(f'Seu peso em Urano é: {peso}')