# Crie uma função que determine se um número é perfeito.
n = int(input('Digite um numero: '))


def perfeito(n):
    soma = 0
    for val in range(1, n):
        if n % val == 0:
            soma += val

    if soma == n:
        print('É perfeito')
    else:
        print('Nao é perfeito')


perfeito(n)
