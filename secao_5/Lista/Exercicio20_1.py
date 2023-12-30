preco = int(input('Digite um preço de um produto: '))
acrescimo = int(input('Digite um porcentual de acréscimo: '))

valor = (preco / acrescimo) + preco

print(f'O valor de venda é R${valor}')

