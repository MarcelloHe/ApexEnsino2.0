# Faça um programa que leia 5 números e informe o maior número.
def maior_numero():
    lista_numero = list()
    for i in range(5):
        numero = int(input('Digite um numero: '))
        lista_numero.append(numero)
    maior = max(lista_numero)
    print(
        f'Os numeros digitado foram {lista_numero} e o maior numero foi {maior}')


maior_numero()
