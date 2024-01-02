n = int(input('Digite um valor de três digitos: '))

centenas = n // 100
dezenas = n % 100 // 10
unidade = n % 10

print(f'O número que você escolheu é: {n} e o inverso dele é: {unidade}{dezenas}{centenas}')

strn = str(n)
print(f'Valor invertido: {"".join(reversed(strn))}')