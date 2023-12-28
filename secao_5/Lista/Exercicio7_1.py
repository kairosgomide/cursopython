duracao_evento_segundos = int(input('Digite a duração de um evento em segundos: '))

horas = duracao_evento_segundos // 3600
resto_minutos = duracao_evento_segundos % 3600
minutos = resto_minutos // 60
segundos = resto_minutos % 60

print(f'Esse evento tem exatamante {horas} horas, {minutos} minutos e {segundos} segundos de duração')