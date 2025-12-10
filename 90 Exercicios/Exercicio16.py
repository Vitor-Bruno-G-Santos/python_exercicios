#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))
num3 = int(input("Digite o numero 3: "))

if(num1 <= num2 and num1 <= num2):
    print("Menor:", num1)
elif(num2 <= num1 and num1 <= num3):
    print("Menor:", num2)
else:
    print("Menor:", num3),

if(num1 >= num2 and num1 >= num2):
    print("Maior:", num1)
elif(num2 >= num1 and num1 >= num3):
    print("Maior:", num2)
else:
    print("Maior", num3)