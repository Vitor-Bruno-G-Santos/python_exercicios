numeroConta = int(input("Digite o numero da conta: "))
saldo = float(input("Digite o saldo: "))
debito = float(input("Digite o valor dos debitos: "))
credito = float(input("Digito o valor dos creditos: "))

saldo = saldo - debito + credito

if(saldo >= 0):
    print("Saldo positivo:", saldo)
else:
    print("Saldo negativo", saldo)