# Faça um programa que leia e valide as seguintes informações:
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';

def validando_cadastro():
    while True:
        nome = str(input('Digite seu nome: '))
        idade = int(input('Digite sua idade: '))
        salario = float(input('Digite seu salario: '))
        sexo = str(input('Digite seu sexo: ')).upper()
        estado_civil = str(input('Digite seu estado civil: ')).upper()
        if len(nome) < 3:
            print('Nome tem que ser maior que 3 caracteres')
        else:
            print(nome)
            if idade < 0 or idade > 150:
                print('Idade tem que ser entre: 0 e 150')
            else:
                print(idade)
                if salario < 0:
                    print('Salario tem que ser maior que: 0')
                else:
                    print(salario)
                    if sexo != 'F' and sexo != 'M':
                        print('Sexo tem que ser: F ou M')
                    else:
                        print(sexo)
                        if estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
                            print(
                                'Estado civil tem que ser entre: S de solteiro, C de casado, V de viuvo, D de divorciado')
                        else:
                            print(estado_civil)

                            break


validando_cadastro()
