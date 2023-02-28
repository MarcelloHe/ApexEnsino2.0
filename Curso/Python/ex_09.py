# Escreva uma função que calcule a soma dos números de 1 a N.
# Ex: (N=5) => (1+1)+(1+2)+(1+3)+(1+4)+(1+5) ...
n = int(input('Dgitie um numero'))


def calcular(n):

    for i in (range(1, n)):
        print('1 + ', i, ' = ', i+1)


print(calcular(n))
