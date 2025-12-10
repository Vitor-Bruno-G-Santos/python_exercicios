#Faça um Programa que peça os 3 lados de um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))
 

if lado1 == lado2 and lado2 == lado3:
    print("Triangulo equilatero")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Triangulo escaleno")
else:
    print("Triangulo isoceles")