palavras = []
def analisar_palavras(palavras : list):
    vogais = "aiueoAIUEO"
    palavraVogal = 0
    for i in palavras:
        for j in vogais:
            if i[0] == j:
                palavraVogal += 1
    palavraLonga = max(palavras, key=len)
    return f"ANALISE DAS PALAVRAS\n---------------------\nPalavras que começam com vogal: {palavraVogal}\nPalavra mais longa: {palavraLonga}"

def palavras_digitadas():
    while True:
        
        quantPalavras = int(input("0 - Sair\nQuantas palavras serão digitadas: "))
        if quantPalavras == 0:
            return
        else:
            for i in range(quantPalavras):
                palavras.append(str(input(f"Digite a {i + 1}º palavra: ")))

            print(analisar_palavras(palavras))
    

def Main():
    
    palavras_digitadas()

Main()
print(palavras)