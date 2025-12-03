#Leia a temperatura em Celsius e informe se o clima está frio, agradável ou quente.

while True:
    try:
        temperatura = float(input("Digite a temperatura em Celsius: "))

        if temperatura < 20:
            print("Frio")
        elif temperatura <= 26:
            print("Agradável")
        else:
            print("Calor")
        

        break
    except ValueError:
        print("Valor invalido")