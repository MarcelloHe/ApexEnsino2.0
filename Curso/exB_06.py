# Faça um Programa que peça dois números e imprima a soma.
def pedir_numeros():
    lista_numeros = list()
    for i in range(2):
        numeros = float(input('Digite um numero: '))
        lista_numeros.append(numeros)
    return lista_numeros


def soma():
    numeros = pedir_numeros()
    soma = sum(numeros)
    print(f'Os numeros informados foram {numeros} e a soma é {soma}')


soma()
