#Leia altura e peso, calcule o IMC e classifique o resultado de acordo com as categorias estabelecidas.

while True:
    try:
        altura = float(input("Digite a sua altura em metros: "))
        peso = float(input("Digite o seu peso: "))

        imc = peso / (altura * altura) 

        if imc > 0 and imc < 18.5:
            print(f"Abaixo do peso\nIMC = {imc}")
        
        elif imc >= 18.5 and imc < 25:
            print(f"Peso normal\nIMC = {imc}")

        elif imc >= 25 and imc < 30:
            print(f"Sobrepeso\nIMC = {imc}")
        
        elif imc >= 30 and imc < 35:
            print(f"Obesidade grau 1\nIMC = {imc}")

        elif imc >= 35 and imc < 40:
            print(f"Obesidade grau 2\nIMC = {imc}")

        elif imc >= 40:
            print(f"Obesidade grau 3\nIMC = {imc}")
        
        break

    except ValueError:
        print("O valor digitado não é um numero")