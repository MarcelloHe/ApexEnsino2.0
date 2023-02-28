# Escreva uma função que verifique se um número é primo.
def num_primo():

    num = int(input('Verificar se número é primo: '))
    contador, divisores = 1, 0
    while True:
        if num % contador == 0:  # Verifica se não sobra resto na divisão do num pelo contador.
            # Se não sobrou, adiciona + 1 para variável divisores.
            divisores += 1
        contador += 1  # Depois do if, aumenta + 1 no contador
        # Se o contador for igual o número + 1 que vc quis verificar, entre neste bloco.
        if contador == num+1:
            # Verifica se tem só 2 divisores (Dividido por 1 e por ele mesmo).
            if divisores == 2:
                print('É primo.')
                break  # Se for primo, diga que é primo e pare o programa.
        else:
            print('Não é primo.')
            break  # Senão, diga que não é primo e pare o programa


num_primo()
