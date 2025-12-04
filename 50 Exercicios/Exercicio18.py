# Leia um número inteiro e exiba sua tabuada completa de 1 a 10.

while True:
    try:

        numero = int(input("Digite um numero inteiro: "))
        for i in range(1, 11):
            print(numero * i)

    except ValueError:
        print("O valor digitado não é inteiro ou não é um numero")