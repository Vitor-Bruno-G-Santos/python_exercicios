#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este é bissexto.

ano = int(input("Digite o ano"))

print("É bissexto" if ano % 4 == 0 else "Não é bissexto")