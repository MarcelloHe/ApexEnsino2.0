# Escreva uma função que conte quantas vezes uma determinada palavra ocorre em uma string.

texto = input('Adicione um texto ')
palavra_verifica = input('Qual palavra deseja verificar ')


def verifica_string(texto, palavra_verifica):
    palavras = texto.split()

    return palavras.count(palavra_verifica)


print(
    f'A palavra {palavra_verifica} foi usada {verifica_string(texto, palavra_verifica)}x')
