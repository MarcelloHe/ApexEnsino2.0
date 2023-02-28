# Escreva uma função que determine se um número é positivo, negativo ou zero.
n = float(input('Digite um numero: '))


def testando_numero(n):
    if n > 0:
        print(f'O numero {n} é positivo ')
    elif n < 0:
        print(f'O numero {n} é negativo ')
    else:
        print(f'O numero {n} é 0 ')


testando_numero(n)
