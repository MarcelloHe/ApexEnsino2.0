# Escreva uma função que retorne a soma dos elementos de uma lista.
def soma_numeros():
    numeros = list()
    while True:
        n = int(input('Digite um valor: '))
        numeros.append(n)
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break
    soma = sum(numeros)
    print(f'A soma é {soma}')


soma_numeros()
