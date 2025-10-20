#Exercicio 1

'''moneyPerHour = float(input("Digite o quanto ganha por hora: "))
workedTime = int(input("Digite as horas trabalhadas por mes: "))

print("Salario bruto: ", moneyPerHour * workedTime)'''

#Exercicio 2

'''num1 = int(input("Digite o 1° numero inteiro: "))
num2 = int(input("Digite o 2° numero inteiro: "))
num3 = float(input("Digite o numero real: "))

print("Resultado 1: ", (num1 * 2) * (num2 / 2))
print("Resultado 2: ", (num1 * 3) + num3)
print("Resultado 3: ", num3 * num3 * num3)'''

#Exercicio 3

'''altura = float(input("Digite sua altura  em metros: "))

print("Peso ideal se homem: ", (72.7 * altura) - 58)
print("Peso ideal se mulher: ", (62.1 * altura) - 44.7)'''

#Exercicio 4

'''pesoPeixe = float(input("Digite a quantidade de peixe em KG: "))    
if pesoPeixe > 50:
    print("Multa: ", (pesoPeixe - 50) * 4)
else:
    print("Sem multa")'''

#Exercicio 5

'''moneyPerHour = float(input("Digite o quanto ganha por hora: "))
workedTime = int(input("Digite as horas trabalhadas por mes: "))
inss = (moneyPerHour * workedTime) * 0.08
sindicate = (moneyPerHour * workedTime) * 0.05
ir = (moneyPerHour * workedTime) * 0.11

print("Salario bruto: ", moneyPerHour * workedTime)
print("INSS: ", inss)
print("Sindicato: ", sindicate)
print("Salario liquido", (moneyPerHour * workedTime) - sindicate - ir - inss)'''

#Exercicio 6

'''tamanhoArquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidadeInternet = float(input("Digite a velocidade da internet em Mbps: "))
tempoDecimal = ((tamanhoArquivo / (velocidadeInternet / 8))) / 60
tempoMinutos = (60 * (tempoDecimal - int(tempoDecimal))) /  100

print("Tempo estimado de download: ", tempoMinutos + int(tempoDecimal))'''