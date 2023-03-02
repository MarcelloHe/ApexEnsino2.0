# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
def imprimir_impar():
    lista_impar = list()
    for i in range(50):
        if i % 2 == 1:
            lista_impar.append(i)
    print(f'A lista de numeros impares entre 1 e 50 é {lista_impar}')


imprimir_impar()
