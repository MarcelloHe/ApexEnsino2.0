# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def pedir_numero():
    numero = float(input('Digite um numero: '))
    return numero


def mostrar_numero():
    numero = pedir_numero()
    print(f'O numero que voce digitou foi: {numero}')


mostrar_numero()
