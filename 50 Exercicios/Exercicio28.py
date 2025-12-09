#Leia uma quantidade n de valores inteiros e exiba apenas aqueles que forem múltiplos de 3.

while True:
    try:
        numeros = 0
        mult3 = []

        quantNumeros = int(input("Quantos numeros deseja informar? "))
        for i in range(quantNumeros):
            numeros = int(input(f"Digite o {i + 1}º numero: "))
            if numeros % 3 == 0:
                mult3.append(numeros)
    
        print("Numeros multiplos de 3 que foram digitados", mult3)
        break
    except ValueError:
        print("O valor digitado não é um numero inteiro")