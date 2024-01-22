x = int(input('Dê um valor para X: '))

if x <= 1:
    print(f'f(x) = 1')
elif x > 1 and x <= 2:
    print(f'f(x) = 2')
elif x > 2 and x <= 3:
    print(f'f(x) = {x ** 2}')
else:
    print(f'f(x) = {x ** 3}')

