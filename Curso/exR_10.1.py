# Altere o programa anterior para mostrar no final a soma dos números.


def intervalo_numeros():
    lista = list()
    n1 = int(input('Digite o numero inicial: '))
    n2 = int(input('Digite o numero final: '))
    percorre = range((n1+1), n2)
    for n in percorre:
        print(n)
        lista.append(n)
    print('A soma é: ', sum(lista))


intervalo_numeros()
