# Crie uma aplicação que calcule o IMC do indivíduo, pesquise a fórmula e aplique.

def calculo_imc():
    peso = float(input('Digite seu peso em Kg: '))
    altura = float(input('Digite sua altura em metros: '))
    imc = peso / altura ** 2
    return imc


def tabela_imc():
    imc = calculo_imc()
    if imc >= 18.5 and imc < 25:
        print(f'Seu IMC foi {imc:.2f} resultado: Normal')
    elif imc > 25 and imc < 30:
        print(f'Seu IMC foi {imc:.2f} resultado: Sobrepeso')
    elif imc >= 30 and imc < 40:
        print(f'Seu IMC foi {imc:.2f} resultado: Obesidade')
    else:
        print(f'Seu IMC foi {imc:.2f} resultado: Obesidade Grave')


tabela_imc()
