total_dias = int(input('Escreva o total dias de você já viveu '))

anos = total_dias // 365
resto_mes = total_dias % 365
meses = resto_mes //  30
dias = resto_mes % 30
print(f'Você já viveu {anos} anos, {meses} meses, {dias} dias ')
