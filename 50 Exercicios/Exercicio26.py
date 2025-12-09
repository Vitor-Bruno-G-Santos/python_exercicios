#Leia uma lista de números inteiros e gere outra lista contendo apenas os números positivos. Exiba ambas as listas.

while True:
    numerosInteiros = []
    numerosInteirosPositivos = []
    try:
        
        tamLista = int(input("Digite a quantidade de numeros que irá digitar: "))

        for i in range(tamLista):
            numerosInteiros.append(int(input(f"Digite  o {i + 1}º numero: ")))
        for i in numerosInteiros:
            if i > 0:
                numerosInteirosPositivos.append(i)
        
        print("Todos os numeros:", numerosInteiros)
        print("Numeros positivos:", numerosInteirosPositivos)
        break

    except ValueError:
        print("O valor digitado não é um numero inteiro")