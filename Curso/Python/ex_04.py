# Crie uma função que retorne o maior elemento de uma lista de números.
def maior_num():

    numeros = list()
    while True:
        n = int(input('Digite um valor: '))
        numeros.append(n)
        r = str(input('Quer continuar? [S/N] '))
        if r in 'Nn':
            break
    maior_num = max(numeros)
    print(f'O maior numero que voce digitou foi {maior_num} ')


maior_num()
