#Leia uma frase e exiba todas as palavras em ordem alfabética.


palavras = []
frase = str(input("Digite a frase: "))
pos = 0
frase = frase.strip()
for i in range(len(frase)):
    frase = frase.replace("  "," ")

for i in range(len(frase)):
    if frase[i] != frase[-1] and i != 0:
        if frase[i] == " " and (frase[i - 1] != " " and frase[i + 1] != " "):
            palavras.append(frase[pos:i])
            pos = i + 1
    
palavras.append(frase[pos:len(frase)])
    
palavras.sort()
print(palavras)