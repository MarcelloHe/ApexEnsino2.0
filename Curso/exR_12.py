# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares

def soma_par_impar():
    lista_par = list()
    lista_impar = list()
    for i in range(10):
        numero = int(input('Digite um numero: '))
        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)
    print('A quantidade de numeros pares é :', len(lista_par))
    print('A quantidade de numeros impares é :', len(lista_impar))


soma_par_impar()
