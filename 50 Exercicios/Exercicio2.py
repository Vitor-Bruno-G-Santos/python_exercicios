#Leia três números reais e determine qual deles é o maior. Em caso de igualdade, informe adequadamente.
while True:
    try:
        num = []
        valores = 0
        for i in range(3):
            num.append(int(input(f"Digite o {i + 1}° numero: ")))

        for i in range(len(num)):
            if max(num) == num[i]:
                valores += 1

        print(f"Maior numero: {max(num)}")

        print(f"Numeros repetidos: {valores}") if valores > 1 else print("Não tem numeros repetidos")
        break
    except ValueError:
        print("Valor digitado não é um numero real")