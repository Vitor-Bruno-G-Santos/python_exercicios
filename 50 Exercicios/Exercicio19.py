#Leia vários nomes (quantidade definida pelo usuário) e ao final exiba o total de nomes, o maior nome e o menor nome em quantidade de caracteres.

while True:
    try:
        
        nomes = []
        menorNome = "" 
        maiorNome = ""

        quantidadeNomes = int(input("Digite a quantidade de nomes que deseja informar: "))

        for i in range(quantidadeNomes):
            nomes.append(str(input(f"Digite o {i + 1}° nome: ")))

        for i in nomes:
            print(i)
            if i == min(nomes):
                menorNome = i
            elif i == max(nomes):
                maiorNome = i
        
        print("Menor nome:", menorNome)
        print("Maior nome:", maiorNome)
    except ValueError:
        print("O valor digitado não é valido")