# Leia um número inteiro positivo e exiba todos os números de 1 até ele, além da soma total desses valores.

while True:
    try:

        numero = int(input("Digite um numero inteiro positivo: "))

        if numero > 0:
            total = 0
            for i in range(1, numero + 1):
                total += i
                print(i)
            print("Total:", total)
            break
        else:
            print("O numero não é inteiro")

    except ValueError:
        print("O valor digitado não é inteiro ou não é um numero")