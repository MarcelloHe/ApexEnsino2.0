# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
def calcula_area_dobra():
    lado = float(input('Digite um lado do quadrado: '))
    area = lado ** 2
    dobro_area = area * 2
    print(f'A area é {area} e o dobro dela fica {dobro_area} ')


calcula_area_dobra()
