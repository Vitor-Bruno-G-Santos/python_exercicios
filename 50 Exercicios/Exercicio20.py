# Leia números inteiros até que o usuário digite 0 e ao final exiba a quantidade, a soma, a média, o maior e o menor valor.

numeros = []
soma = 0
while True:
    try:

        numeros.append(int(input("Digite um número inteiro: ")))
        if numeros[-1] == 0:
            numeros.remove(0)
            break

            
    except ValueError:
        print("Isto não é um numero inteiro")

for i in numeros:
    soma += i

print(f"Soma: {soma}\nMédia: {soma / len(numeros)}\nMaior valor: {max(numeros)}\nMenor valor: {min(numeros)}")