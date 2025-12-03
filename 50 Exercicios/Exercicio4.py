#Leia um número inteiro e informe se ele é positivo, negativo ou zero.

try:
    numero = int(input("Digite um numero inteiro: "))

    print("Positivo" if numero > 0 else ("Negativo"if numero < 0 else "Zero"))

except ValueError:
    print("Valor invalido")