while True:
    try:

        ano = int(input("Digite o valor de um ano: "))

        print(f"O ano {ano} é bissexto") if ano % 4 == 0 else print(f"O ano {ano} não é bissexto")
        break
    except ValueError:
        print("Valor digitado não é um numero inteiro")