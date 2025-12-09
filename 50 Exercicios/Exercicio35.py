#Leia um código de operação bancária (depósito, saque, extrato, sair) e exiba apenas mensagens simulando a operação.

while True:
    try:

        opt = int(input("1 - Depósito\n2 - Saque\n3 - Extrato\n0 - Sair\nDigite a opção desejada: "))
        match opt:
            case 1:
                print("Saldo = R$1000\nValor do deposito = R$100\nSaldo final = R$1100")
                input("Aperte enter para sair")
            case 2:
                print("Saldo = R$1000\nValor do saque = R$100\nSaldo final = R$900")
                input("Aperte enter para sair")
            case 3:
                print("---Extrato---\nSaldo: R$500\nDeposito: R$1000\nSaque: R$500\n---------------\nSaldo final: R$1000")
                input("Aperte enter para sair")
            case 0:
                print("Saindo")
                break
            case _:
                print("Opção invalida")

    except ValueError:
        print("O valor digitado não é um numero inteiro")