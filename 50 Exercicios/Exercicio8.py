#Leia um número de 1 a 12 representando um mês e informe o nome do mês correspondente e o trimestre do ano ao qual pertence

while True:
    try:
    
        mes = int(input("Digite o numero do mês: "))
        match mes:
            case 1:
                print("Janeiro\n1° Trimestre")
                break
            case 2:
                print("Fevereiro\n1° Trimestre")
                break
            case 3:
                print("Março\n1° Trimestre")
                break
            case 4:
                print("Abril\n2° Trimestre")
                break
            case 5:
                print("Maio\n2° Trimestre")
                break
            case 6:
                print("Junho\n2° Trimestre")
                break
            case 7:
                print("Julho\n3° Trimestre")
                break
            case 8:
                print("Agosto\n3° Trimestre")
                break
            case 9:
                print("Setembro\n3° Trimestre")
                break
            case 10:
                print("Outubro\n4° Trimestre")
                break
            case 11:
                print("Novembro\n4° Trimestre")
                break
            case 12:
                print("Dezembro\n4° Trimestre")
                break
            case _:
                print("Mês invalido")

    except ValueError:
        print("Valor invalido")