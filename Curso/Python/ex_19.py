# Escreva uma função que retorne o inverso de um número.
numero = int(input('Digite um numero: '))


def inverte_numero(numero):

    numero = str(numero)
    print(numero[::-1])


inverte_numero(numero)
