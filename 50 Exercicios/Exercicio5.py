#Leia o valor de um produto e o tipo de pagamento (1 para à vista, 2 para cartão, 3 para boleto) e calcule o valor final considerando regras diferentes para cada forma de pagamento.
while True:
    try:
        produto = float(input("Digite o valor "))
        tipoPagamento = int(input("1 - À vista | 10% desconto\n2 - Cartão | Sem desconto\n3 - Boleto | 5% desconto\nDigite o numero correspondente a forma de pagamento: "))
        
        match tipoPagamento:
            case 1:
                print(f"Valor a ser pago: {produto * 0.9}\nPagamento a vista")
            case 2:
                print(f"Valor a ser pago: {produto}\nPagamento no cartão")
            case 3:
                print(f"Valor a ser pago: {produto * 0.95}\nPagamento no boleto")
            case _:
                produto / 0

        break
    except ValueError:
        print("Numero digitado invalido ou isto não é um numero")
    except ZeroDivisionError:
        print("Opção digitada não encontrada")