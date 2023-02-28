# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temp = float(input('Digite a temperatura em Celsiu: '))
temp_fah = (temp * 1.8) + 32
print(
    f'A temperatura em graus Fahrenheit é {temp_fah}')
