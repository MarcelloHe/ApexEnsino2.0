

nome = "Jorge"
sobrenome = "de Melo"

nome_completo = nome + " " + sobrenome

print(nome_completo)

print(f" essa é outra forma de juntar as coisas ! {nome} {sobrenome}")

# Operadores Ternários ( Famoso If else )

resultado = "verdadeiro" if 1 == 1 else "false"
print(resultado)

if resultado == "verdadeiro":
    print("o resultado é true")
elif resultado == "falso":
    print("o resultaduo é false")
else:
    print("isso não deveria ter chego até aqui !")


resultado = resultado.replace("verdadeiro", "trocando o primeiro parâmetro pelo segundo")

print(f"text.replace serve para alterar valores de uma string {resultado}")

print(resultado[0:8])

print(resultado.upper())

print(resultado.lower())

print("teste".upper() == "TESTE")
print("teste" == "TESTE")
