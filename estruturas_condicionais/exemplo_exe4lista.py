peso = float(input('Digite o seu peso: '))
numero = int(input('Escreva um número de 1 a 6: '))
planeta = ['MERCÚRIO', 'VÊNUS', 'MARTE', 'JÚPITER', 'SATURNO', 'URANO']
gravidade = [0.37, 0.88, 0.38, 2.64, 1.15, 1.17]

peso_outro_planeta = peso * gravidade[numero-1]

print(f'O seu peso na Terra é: {peso}')
print(f'O seu peso em {planeta[numero-1]} é: {peso_outro_planeta}')