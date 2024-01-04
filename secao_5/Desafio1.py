#5.35 Desafio Operadores Lógicos

trabalho_terca = False
trabalho_quinta = False

'''
- Confirmando os 2: TV 50 + sorvete
- Corfirmando apenas 1: TV 32 + sorvete
- Nenhum confirmado: Fica em casa
'''
if trabalho_terca == True and trabalho_quinta == True:
    print('Vamos comprar uma TV de 50 polegadas e sorvete')
elif trabalho_quinta == True or trabalho_terca == True:
    print('Vamos comprar um TV de 32 polegadas e também sorvetes')
else:
    print('Ficaremos em casa')
