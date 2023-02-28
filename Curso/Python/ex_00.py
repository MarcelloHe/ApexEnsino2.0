# Crie uma função que determine se um número é par ou ímpar.
def par_impar():
    numero = int(input('Digite um numero: '))
    resto = numero % 2
    if resto == 0:
        return print('Esse numero é par')

    return print('Esse numero é impar')


par_impar()
