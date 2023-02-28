# Crie uma função que calcule a média de uma lista de números.
def media_numeros():
    numeros = list()
    while True:
        n = int(input('Digite um valor: '))
        numeros.append(n)
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break
    media = sum(numeros) / len(numeros)
    print(f'A media é de {media}')


media_numeros()
