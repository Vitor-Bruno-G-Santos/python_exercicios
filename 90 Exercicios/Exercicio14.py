#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcule e escreva o saldo atual (saldo atual = saldo - débito + crédito). Também teste se saldo atual for maior ou igual a zero. Em seguida escreva a mensagem 'Saldo Positivo', senão, escrever a mensagem 'Saldo Negativo' .

numeroConta = int(input("Digite o numero da conta: "))
saldo = float(input("Digite o saldo: "))
debito = float(input("Digite o valor dos debitos: "))
credito = float(input("Digito o valor dos creditos: "))

saldo = saldo - debito + credito

if(saldo >= 0):
    print("Saldo positivo:", saldo)
else:
    print("Saldo negativo", saldo)