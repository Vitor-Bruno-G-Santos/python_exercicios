#Leia um número inteiro digitado pelo usuário e garanta que ele só avance quando o número for válido.

while True:
    try:
        int(input("Digite um numero inteiro: "))
        break
    except ValueError:
        print("O valor digitado não é um numero inteiro")