n = int(input('Digite um número para ver se ele é primo ou não: '))
primo = True

for i in range(2, (n**0.5) + 1):
        if n % i == 0:
            primo = False
            break

if primo:
        print(f"{n} é um número primo.")
else:
        print(f"{n} não é um número primo.")
