# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;

#     misturar latas e galões, de forma que o desperdício de tinta seja menor.
#     Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# Exercício 17
# Necessária a importação do módulo math
# math.ceil sempre arredonda para cima, pois não podemos comprar meia lata, somente latas inteiras.
import math
litros_lata = 18
preco_lata = 80
litros_galao = 3.6
preco_galao = 25

m2 = float(input("Por favor, insira o tamanho da área em metros quadrados: "))
litros_necessarios = m2 / 6

# a - apenas latas de 18L
qtd_latas = math.ceil(litros_necessarios / litros_lata)
custo_latas = qtd_latas * preco_lata
print("Somente latas de 18L:")
print(
    f'O cliente precisa comprar {qtd_latas} latas, que custarão R${custo_latas}.')

# b - apenas galões de 3.6L
qtd_galoes = math.ceil(litros_necessarios / litros_galao)
custo_galoes = qtd_galoes * preco_galao
print("Somente galões de 3.6L:")
print(
    f'O cliente precisa comprar {qtd_galoes} galões, que custarão R${custo_galoes}.')

# c - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
litros_necessarios_folga = litros_necessarios * 1.1
qtd_latas_c = litros_necessarios_folga // litros_lata

litros_necessarios_folga_faltando = litros_necessarios_folga - \
    (qtd_latas_c * litros_lata)
qtd_galoes_c = math.ceil(litros_necessarios_folga_faltando / litros_galao)

custo_mix = (qtd_latas_c * preco_lata) + (qtd_galoes_c * preco_galao)

print("Mix de latas e galões:")
print(
    f'O cliente precisa comprar {qtd_latas_c} latas e {qtd_galoes_c} galões, que custarão {custo_mix}')
