# Crie uma função que converta uma lista de números em uma lista de strings.


def converter_lista():
    numeros = list()
    while True:
        n = int(input('Digite um valor: '))
        numeros.append(str(n))
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break

    print(numeros)


converter_lista()
