#  Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

def pedir_nota():
    while True:
        nota = int(input('Digite uma nota entre 0 e 10: '))
        if nota >= 0 and nota <= 10:
            break
        else:
            print('Valor invalido! ')


pedir_nota()
