#Leia um número inteiro n e calcule o fatorial de n.

while True:
    try:
        total = 1
        numero = int(input("Digite um numero inteiro: "))

        for i in range(1, numero + 1):
            total *= i

        print(total)
        break
    except ValueError:
        print("O valor digitado não é um numero inteiro")