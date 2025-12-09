#Leia um valor e uma escala de temperatura (C para Celsius, F para Fahrenheit) e faça a conversão, tratando entradas inadequadas.

while True:
    try:
        option = str(input("C - Celsius\nF - Fahrenheit\nDigite qual escala de temperatura deseja informar: ")).upper()
        
        match option:
            case "C":
                temp = float(input("Agora digite a temperatura: "))
                print("Convertido para Fahrenheit:", (temp * (9/5)) + 32)
            
            case "F":
                temp = float(input("Agora digite a temperatura: "))
                print("Convertido para Celsius:",(temp - 32) * 5/9)
                
            case _:
                print("Opção invalida")


    except ValueError:
        print("O valor digitado não é um numero")