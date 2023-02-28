
def solicita_numero_ao_user():
    satisfeito = True

    print("Inicio")
    while satisfeito:
        numero = int(input("Contagem regressiva a partir de: "))

        for i in range(numero, 0, -1):
            print(i)

        if input("Digite S para continuar ou N para sair: ").upper() != "S":
            satisfeito = False

    print("Fim")


solicita_numero_ao_user()



