# Leia uma frase e exiba a quantidade de caracteres, a quantidade de espaços e a quantidade de vogais
quantidadeVogais = 0
quantidadeEspaco = 0
while True:
    try:
        vogais = "aiueo"
        espaco = " "
        frase = str(input("Digite uma frase: "))
        for i in frase:
            if i.lower() in vogais:
                quantidadeVogais +=1
            elif i in " ":
                quantidadeEspaco += 1
        break
    except ValueError:
        print("Valor digitado é invalido")
print(f"Tamanho da frase: {len(frase)}\nQuantidade de espaços: {quantidadeEspaco}\nQuantidade de vogais: {quantidadeVogais}")