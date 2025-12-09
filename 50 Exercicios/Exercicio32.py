#Leia um número de 1 a 12 e exiba o nome do mês e a estação do ano correspondente.

while True:
    try:
        mes = int(input("Digite o numero do mês: "))
        match mes:
            case 1:
                print("Janeiro\nVerao")
                break
            case 2:
                print("Fevereiro\nVerao")
                break
            case 3:
                print("Março\nOutono")
                break
            case 4:
                print("Abril\nOutono")
                break
            case 5:
                print("Maio\nOutono")
                break
            case 6:
                print("Junho\nInverno")
                break
            case 7:
                print("Julho\nInverno")
                break
            case 8:
                print("Agosto\nInverno")
                break
            case 9:
                print("Setembro\nPrimavera")
                break
            case 10:
                print("Outubro\nPrimavera")
                break
            case 11:
                print("Novembro\nPrimavera")
                break
            case 12:
                print("Dezembro\nVerao")
                break
            case _:
                print("Mês invalido")

    except ValueError:
        print("O valor digitado não é um número inteiro")