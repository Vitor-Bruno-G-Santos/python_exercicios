'''
Um brechó revende produtos usados, e fixa o preço de
venda de cada produto conforme o valor de sua aquisição: Se o
preço de aquisição de um produto é menor que R$ 50,00, ele
deve ser vendido por um preço 45% maior, caso contrário o lucro
será de 30%. Sabendo disso, faça um algoritmo que leia o valor
de aquisição de um produto e mostre o seu valor de venda.'''

produto = str(input("Digite o valor do produto: "))

if produto > 50:
    print(f"Valor venda produto: {produto * 1.45}")
else:
    print(f"Valor venda produto: {produto * 1.3}")
    