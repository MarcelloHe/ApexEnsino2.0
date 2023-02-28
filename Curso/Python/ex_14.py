# Crie uma função que retorne todos os números pares de uma lista.
def lista_de_par():
    numeros = list()
    while True:
        n = int(input('Digite um numero: '))
        if n % 2 == 0:
            numeros.append(n)
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break
    print(numeros)


lista_de_par()
