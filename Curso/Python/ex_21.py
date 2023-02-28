# Escreva uma função que verifique se duas strings são anagramas.
# Ex: 1) Pedra  2) Perda == True
palavra1 = input('Digite a primeira palavra: ')
palavra2 = input('Digite a segunda palavra: ')


def verifica_anagrama(palavra1, palavra2):

    palavra1_verificada = sorted(palavra1)
    palavra2_verificada = sorted(palavra2)

    print(palavra1_verificada, palavra2_verificada)

    if (palavra1_verificada == palavra2_verificada):
        print('Essas palavras sao anagramas ')


verifica_anagrama(palavra1, palavra2)
