import random

media = []
for n in range (1, 13):
    kwh = random.randint(120, 380)
    media.append(kwh)

media_final = sum(media) / len(media)
print(media_final)

if media_final <= 172:
    print('Bandeira: Verde')
elif media_final > 172 and media_final <= 280:
    print('Bandeira Amarela')
else:
    print('Bandeira: Vermelha')