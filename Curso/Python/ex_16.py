# Crie uma função que calcule a soma dos números pares de 1 a N

n = int(input('Dgitie um numero'))


def calcular(n):
    numeros = list()
    for i in (range(1, n)):
        resto = i % 2
        if resto == 0:
            numeros.append(i)
    print(f'Os numeros pares sao {numeros} e a soma é {sum(numeros)}')


calcular(n)
