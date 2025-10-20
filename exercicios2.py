#Exercicio 1

'''raio = float(input("Digite o raio: "))
print("Area do circulo: ", 3.14 * (raio * raio))'''

#Exercicio 2

'''lado = float(input("Digite o valor de um lado: "))
print("Area: ", lado * lado)
print("Dobro da Area: ",2 * (lado * lado))'''

#Exercicio 3

'''ano = int(input("Digite o ano: "))
if ano % 4 == 0:
    print("Ano Bissexto")
else:
    print("Não é ano bissexto")'''

#Exercicio 4

'''temperatura = float(input("Digite a temperatura  em Celsius: "))
print("Ao converter a temperatura que digitou para Fareneheit resulta em: ", temperatura * (9/5) + 32)'''

#Exercicio 5

'''valorConta = float(input("Digite valor da conta: "))
valorGorjeta = int(input("Digite o valor da porcentagem da gorjeta: "))

print("Valor da gorjeta: ", valorConta * (valorGorjeta /  100))
print("Valor total a ser pago: ", valorConta + (valorConta * (valorGorjeta / 100)))'''

#Exercicio 6

'''tempoMinutos = int(input("Digite o tempo em minutos: "))
tempoDecimal = tempoMinutos / 60
tempoHoras = ((tempoDecimal - int(tempoDecimal)) * 60) / 100
print("Tempo em horas: ", int(tempoDecimal) + tempoHoras)'''

#Exercicio 7

'''valorCompra = float(input("Digite o valor da compra: "))
porcentagemDesconto = int(input("Digite a porcentagem do desconto: "))
valorDesconto = valorCompra * (porcentagemDesconto / 100)

print("Valor do desconto: ", valorDesconto)
print("Valor compra com desconto: ", valorCompra - valorDesconto)
print("Você economizou R$", valorDesconto)'''

#Exercicio 8

'''valorEmReais = float(input("Digite que deseja converter o valor em Reais: "))
tipoMoeda = str(input("Digite a moeda desejada: \n (D) - Para dolar\n (E) - Para euro\n"))

if tipoMoeda == "D" or tipoMoeda == "d":
    print("Valor em dolar: ", valorEmReais / 5.2 )

elif tipoMoeda == "E" or tipoMoeda == "e": 
    print("Valor em euro: ", valorEmReais / 5.5)

else:
    print("Moeda não encontrada")'''

#Exercicio 9

'''distanciaViagem = float(input("Digite a distancia da viagem: "))
tempoViagem = float(input("Digite o tempo de viagem: "))

print("Velocidade media: ", distanciaViagem / (tempoViagem / 60))'''

#Exercicio 10

'''valorInicial = float(input("Digite o valor investimento inicial: "))
taxaJuros = float(input("Digite o valor da taxa de juros ao mes: "))
tempo = int(input("Digite o tempo em meses: "))

print("Total em juros = ", (valorInicial * taxaJuros * tempo) / 100)'''