#Leia um número inteiro e exiba o resultado da divisão de 100 por esse número, tratando o caso de divisão por zero ou entrada inválida.

while True:
    try:

        numero = int(input("Digite um numero inteiro: "))
        print(100 / numero)
        break

    
    except ValueError:
        print("O valor digitado não é um numero inteiro")
    
    except ZeroDivisionError:
        print("O valor não pode ser 0")