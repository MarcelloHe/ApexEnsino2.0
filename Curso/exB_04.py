# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def pedir_msg():
    msg = str(input('Digite uma mensagem: '))
    return msg


def mostrar_msg():
    msg = pedir_msg()
    print(msg)


mostrar_msg()
