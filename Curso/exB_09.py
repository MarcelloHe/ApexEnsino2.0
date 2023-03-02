# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def calcula_circulo():
    raio = float(input('informe o raio em Cms do circulo:'))
    area = 3.14 * (raio ** 2)
    print(f'A area do circulo é {area}')


calcula_circulo()
