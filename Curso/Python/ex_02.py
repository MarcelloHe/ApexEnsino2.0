# Crie uma função que verifique se uma string é um palíndromo.
def palindromo(palavra):
    tamanho = len(palavra)
    if tamanho == 0:
        # Se a string é vazia, ela é ou não é palíndromo? Estou considerando que não
        return print('Digite alguma palavra')
    for i in range(0, tamanho // 2):
        # encontrei diferença, nem precisa continuar
        if palavra[i] != palavra[tamanho - i - 1]:
            return print('Essa palavra nao é um palindromo')
    return print('Essa palavra e um palindromo')


palindromo(input('Digite uma palavra: '))
