# Faça um programa que leia 5 números e informe a soma e a média dos números.

def soma_media():
    lista_numero = list()
    for i in range(5):
        numero = int(input('Digite um numero: '))
        lista_numero.append(numero)
    soma = sum(lista_numero)
    media = soma / len(lista_numero)
    print(
        f'Os numeros digitado foram {lista_numero} a soma foi {soma} e a  media foi {media}')


soma_media()
