# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#  mostrando uma mensagem de erro e voltando a pedir as informações.

def login():
    while True:
        nome = str(input('Digite seu nome: ')).upper()
        senha = str(input('Digite sua senha: ')).upper()
        if nome == senha:
            print('Erro: senha igual ao nome do usuário')
        else:
            break


login()
