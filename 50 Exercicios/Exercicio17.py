# Leia 10 números inteiros e informe quantos deles são pares e quantos são ímpares.
while True:
    try:
        numeros = []
        parImpar = [0, 0]
        for i in range(10):
            numeros.append(int(input(f"Digite o {i + 1}° valor: ")))
            if numeros [i] % 2 == 0:
                parImpar[0] += 1
            else:
                parImpar[1] += 1

        print("Par:", parImpar[0])
        print("Impar:", parImpar[1])
        break

    except ValueError:
        print("Valor digitado não é inteiro ou não é um numero")