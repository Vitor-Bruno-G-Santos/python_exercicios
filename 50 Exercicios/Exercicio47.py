#Leia nomes completos de várias pessoas e ao final exiba quantas foram cadastradas, quantas começam com uma letra informada e a lista ordenada alfabeticamente.

nomes = []

while True:
    try:
        nomesComInicial = 0
        inicial = ""
        
        quantidadeNomes = int(input("Digite a quantidade de nomes que deseja informar: "))
        for i in range(quantidadeNomes):
            nomes.append(str(input("Digite o nome: ")))
        while True:
            try:
                inicial = str(input("Digite a inicial que deseja procurar: "))
                if len(inicial) != 1:
                        9 / 0
                else:
                    break
            except ZeroDivisionError:
                print("O valor digitado não é uma letra unica")
        for i in nomes:
            if i[0].upper() == inicial.upper():
                nomesComInicial += 1
            
        nomes.sort()
        print(f"Quantidade de pessoas cadastradas: {len(nomes)}\nNomes com a inicial ({inicial}): {nomesComInicial}\nNomes digitados: {nomes}")
        break
    except ValueError:
        print("O valor informado não é um numero inteiro")