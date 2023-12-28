print('Você ira em uma loja de roupas, comprar quantidades diferentes de camisetas e de diferentes tamanhos, na loja tem um catalogo falando o preço das roupas: PEQUENO -- R$10, MÉDIO -- R$12, GRANDE -- R$15 e que se a compra passar de R$150 reais ganha 10% de desconto na sua compra')

pequenas = int(input('Escreva a quantidade de roupas do tamnho pequeno, você deseja comprar: '))
medias = int(input('Escreva a quantidade de roupas do tamnho médio, você deseja comprar: '))
grandes = int(input('Escreva a quantidade de roupas do tamnho grande, você deseja comprar: '))

valor_total = pequenas * 10 + medias * 12 + grandes * 15

if valor_total <= 150:
    print(f'Sua compra deu R${valor_total}')
elif valor_total > 150:
    print(f'Sua compra deu R${valor_total - (valor_total / 10)} com desconto')
else:
    print('ocorreu um problema')


