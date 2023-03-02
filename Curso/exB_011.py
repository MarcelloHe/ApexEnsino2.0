#  Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def salario():
    valor = float(input('Quanto vc ganha por hora: '))
    hora = float(input('Quantas horas vc trabalhou: '))
    salario = valor * hora
    print(f'Seu salario esse mes vai ser {salario}')


salario()
