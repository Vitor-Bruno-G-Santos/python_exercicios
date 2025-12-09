#Leia vários números até que o usuário digite uma palavra-chave para encerrar. Ao final, exiba a quantidade, soma, média, maior e menor valor.
numeros = []
soma = 0
while True:
    try:
        numero = float(input("0 - Sair\nDigite um numero: "))
        if numero == 0:
            break
        else:
            numeros.append(numero)
            soma += numero

    except ValueError:
        print("O valor digitado não é um numero")
print(f"Quantidade de numeros: {len(numeros)} {numeros}\nSoma = {soma}\nMedia = {soma / len(numeros)}\nMenor valor = {min(numeros)}\nMaior valor = {max(numeros)}")