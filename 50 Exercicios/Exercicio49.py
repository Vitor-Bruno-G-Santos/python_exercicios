#Leia uma lista de produtos com nome e preço e exiba o produto mais caro, o mais barato, o preço médio e a lista ordenada pelo nome.
produtos = []
medio = 0
indiceMenor = 0
indiceMaior = 0
quantidadeProdutos = 0
while True:
    try:

        nomeProduto = str(input("Digite o nome do produto: "))
        precoProduto = float(input("Digite o valor do produto: "))
        produtos.append({"NOME":nomeProduto,
                         "PRECO":precoProduto})
        quantidadeProdutos += 1
        medio += precoProduto
        sair = int(input("Deseja sair?\n0 - Sair\n1 - Não sair"))
        if sair == 0:
            medio /= quantidadeProdutos
            break

    except ValueError:
        print("O valor digitado não é um numero inteiro")
if len(produtos) != 0:
    menorValor = produtos[0].get("PRECO")
    maiorValor = produtos[0].get("PRECO")
    for i, j in enumerate(produtos):
        if j.get("PRECO") < menorValor:
            menorValor = j.get("PRECO")
            indiceMenor = i
        if j.get("PRECO") > maiorValor:
            maiorValor = j.get("PRECO")
            indiceMaior = i

        
    print(f"Produto mais caro: {produtos[indiceMaior]}\nProduto mais barato: {produtos[indiceMenor]}\nPreço medio: {medio}\nProdutos: {sorted(produtos, key=lambda x: x["NOME"])}")