while True:
    try:
        
        idade = int(input("Digite a sua idade: "))

        if idade > 0 and idade < 12:
            print("Criança")
        elif idade >= 12 and idade <= 17:
            print("Adolescente")
        elif idade >= 18 and idade <= 59:
            print("Adulto")
        elif idade >= 60 and idade <=120:
            print("Idoso")
        else:
            print("Idade invalida")
        break
    except ValueError:
        print("Valor invalido")