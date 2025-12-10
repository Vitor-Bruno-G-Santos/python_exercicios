'''A lanchonete GostoSoft vende apenas um tipo de sanduíche,
cujo recheio inclui duas fatias de queijo, uma fatia de presunto e
uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou
presunto pesa 50 gramas, e que a rodela de hambúrguer pesa
100 gramas, faça um algoritmo em que o dono forneça a
quantidade de sanduíches a fazer, e a máquina informe as
quantidades (em quilos) de queijo, presunto e carne necessários
para compra.'''

while True:
    try:
        queijoOuPresunto = 0.05
        hamburguer = 0.1

        quantidadeSanduiches = int(input("Digite a quantidade de sanduiches que irá ser produzida: "))
        print(f"Carne: {quantidadeSanduiches * hamburguer}Kg\nQueijo: {quantidadeSanduiches * queijoOuPresunto}Kg\nPresunto: {quantidadeSanduiches * queijoOuPresunto}Kg")


    except ValueError:
        print("O valor digitado não é um numero inteiro")