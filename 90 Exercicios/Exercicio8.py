#Faça um algoritmo que calcule o custo estimado de uma viagem de carro. Posteriormente imprima o resultado.

valorGasolina = float(input("Qual o valor da gasolina: "))
distancia = float(input("Digite a distancia da viagem: "))
autonomiaCarro = float(input("Digite a media que seu carro faz na rodovia: "))

print("Gasto da viagem:", valorGasolina * (distancia / autonomiaCarro))