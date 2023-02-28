# Crie uma função que calcule a potência de um número X elevado a Y.
import math

n = float(input('Digite o valor de N: '))
y = float(input('Digite o valor de Y: '))


def potencia(n, y):
    print(math.pow(n, y))


potencia(n, y)
