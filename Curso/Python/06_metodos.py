
def soma_numeros(num1, num2=100, deve_multiplicar=False):

    if deve_multiplicar:
        return num1 * num2

    return num1 + num2


primeiro = input("informe um número qualquer: ")

segundo = input("informe um número qualquer: ")

resultado = (primeiro, segundo)

print(f"e o resultado será: {resultado}")

outro_resutlado = soma_numeros(int(primeiro), int(segundo))

print(f"agora o resultado é: {outro_resutlado}")

outro_resultado_soma = soma_numeros(num1=25, num2=224)

outro_resultado_soma = soma_numeros(num1=int(primeiro))

print(outro_resultado_soma)