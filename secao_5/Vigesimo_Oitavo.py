#7.76 Desafio IF ELSE

'''
nota = float(input('Digite a nota de um aluno: '))
nota = float

if nota <= 10.0 or nota >= 9.1:
    print('Nota: A')
elif nota <= 9.0 or nota >= 8.1:
    print('Nota: A-')
elif nota <= 8.0 or nota >= 7.1:
    print('Nota: B')
elif nota <= 7.0 or nota >= 6.1:
    print('Nota: B-')
elif nota <= 6.0 or nota >= 5.1:
    print('Nota: C')
elif nota <= 5.0 or nota >= 4.1:
    print('Nota: C-')
elif nota <= 4.0 or nota >= 3.1:
    print('Nota: D')
elif nota <= 3.0 or nota >= 2.1:
    print('Nota: D-')
elif nota <= 2.0 or nota >= 1.1:
    print('Nota: E')
elif nota <= 1.0 or nota >= 0.0:
    print('Nota: E-')
else:
    print('Nota Invalida')
''' 

nota = float(input('Digite a nota de um aluno: '))

if nota > 10:
     print('Nota Invalida')
elif nota >= 9.1:
    print('A')
elif nota >= 8.1:
    print('A-')
elif nota >= 7.1:
    print('B')
elif nota >= 6.1:
    print('B-')
elif nota >= 5.1:
    print('C')
elif nota >= 4.1:
    print('C-')
elif nota >= 3.1:
    print('D')
elif nota >= 2.1:
    print('D-')
elif nota >= 1.1:
    print('E') 
elif nota >= 0.1:
    print('E-')    
else:
    print('Nota Invalida')

if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota(valor_informado)
    print(conceito)


