# Escreva uma função que retorne o menor elemento de uma lista
def menor_num_lista():
    numeros = list()
    while True:
        n = int(input('Digite um numero: '))
        numeros.append(n)
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break
    print(min(numeros))


menor_num_lista()
