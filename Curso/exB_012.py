# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
def celsius_fahrenheit():
    f = float(input('Digite a temperatura em Fahrenheit: '))
    c = (f - 32) * .5556
    print(f'A temperatura em Celsius é {c:.1f}ºC ')


celsius_fahrenheit()
