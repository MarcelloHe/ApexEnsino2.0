# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def pedir_notas():
    lista_notas = list()
    for i in range(4):
        notas = float(input('Digite uma nota: '))
        lista_notas.append(notas)
    return lista_notas


def calcular_media():
    notas = pedir_notas()
    soma_notas = sum(notas)
    media = soma_notas / 4
    print(f'Suas notas foram {notas} e sua media foi {media}')


calcular_media()
