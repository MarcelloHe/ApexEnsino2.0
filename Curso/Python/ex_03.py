# Escreva uma função que ordene uma lista de números de forma crescente.
def numero_cresc():

    numeros = list()
    while True:
        n = int(input('Digite um valor: '))
        numeros.append(n)
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break
    numeros.sort()
    print(f'Voce digitou {numeros} ')


numero_cresc()
