n = int(input('Digite um número: '))
x = 1
y = 4
z = 4
lista = [1, 4, 4]
for i in range(1, n+1):
        x += 1
        y += 1
        z += 1
        lista.append(x)
        lista.append(y)
        lista.append(z)
        
print(lista)