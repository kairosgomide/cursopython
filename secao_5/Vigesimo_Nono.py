#7.78 Desafio ELSE IF

def faixa_etaria(idade):
    if 0 <= idade < 18:
        print('Menor de idade')
    elif idade in range(18, 64):
        print('Adulto')
    elif idade in range(65, 100):
        print('Melhorm idade')
    elif idade >= 100:
        print('Centenário')
    else:
        print('Idade Invalida')

if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}')