# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem

def elevar():
    numero1 = float(input('Digite o numero = base: '))
    numero2 = float(input('Digite o segundo numero = expoente: '))
    calculo = numero1 ** numero2
    print(f'O {numero1} elevado ao {numero2} é {calculo}')


elevar()
