# Faça um algoritmo que receba a lista [4,2,5,6,7,8,1,4,6,7,12] e
# em seguida retorne a lista ao contrário.

#     input = [4,2,5,6,7,8,1,4,6,7,12]
#     output = [12,7,6,4,1,8,7,6,5,2,4]

def inverte_lista():
    lista = [4, 2, 5, 6, 7, 8, 1, 4, 6, 7, 12]
    print(f'A lista que voce digitou foi {lista} ')
    lista.reverse()
    print(f'A lista ao contrario  é {lista} ')


inverte_lista()
