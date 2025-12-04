# Leia um número de 0 a 7 e informe qual dia da semana representa e se é dia útil ou fim de semana.

while True:
    try:

        dia = int(input("Digite o numero de 1 a 7 correspondente ao dia da semana: "))
        match dia:
            case 1:
                print("Segunda-Feira\nDia útil")
                break
            case 2:
                print("Terça-Feira\nDia útil")
                break
            case 3:
                print("Quarta-Feira\nDia útil")
                break
            case 4:
                print("Quinta-Feira\nDia útil")
                break
            case 5:
                print("Sexta-Feira\nDia útil")
                break
            case 6:
                print("Sábado\nFim de semana")
                break
            case 7:
                print("Domingo\nFim de semana")
                break
            case _:
                print("Data invalida")
            

    except ValueError:
        print("O valor digitado não é um numero ou não é um numero valido")