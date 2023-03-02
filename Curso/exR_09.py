# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

def intervalo_numeros():
    n1 = int(input('Digite o numero inicial: '))
    n2 = int(input('Digite o numero final: '))
    percorre = range((n1+1), n2)
    for n in percorre:
        print(n)


intervalo_numeros()
