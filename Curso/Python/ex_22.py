# Escreva uma função que retorne todas as combinações possíveis de uma lista de elementos.

numeros = list()
while True:
    n = input('Digite aqui: ')
    numeros.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break


def comb_possiveis(numeros):
    from itertools import combinations
    temp = combinations(numeros, 2)
    for i in list(temp):
        print(i)


comb_possiveis(numeros)
