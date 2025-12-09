#Leia uma frase, converta-a para maiúsculas, remova espaços nas extremidades e exiba a quantidade de caracteres antes e depois da remoção.


frase = str(input("Digite a frase: ")).upper()
charAntes = len(frase)
frase = frase.strip()
charDepois = len(frase)
print(f"Quantidade de caracteres antes {charAntes}\nQuantidade de caracteres depois {charDepois}\nFrase: {frase}")
