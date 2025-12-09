#Leia uma quantidade n de produtos, com nome e preço, e ao final exiba o total gasto, o produto mais caro e o mais barato.

while True:
    produtos = []
    precoMin = 0
    precoMax = 0
    total = 0
    try:

        quantProdutos = int(input("Digite a quantidade de produtos a serem cadastrados: "))
        
        for i in range(quantProdutos):
            
            nomeProduto = str(input("Digite o nome do produto: "))
            precoProduto = float(input("Digite o preço deste produto: R$"))
            produtos.append({"NOME":nomeProduto,
                            "PRECO": precoProduto})
            precoMin = produtos[i]
            precoMax = produtos[i]
            total += precoProduto
        for i in range(quantProdutos):
            if precoMin.get("PRECO") > produtos[i].get("PRECO"):
                precoMin = produtos[i]
            elif  precoMax.get("PRECO") < produtos[i].get("PRECO"):
                precoMax = produtos[i]
        print(f"Total gasto = {total}")
        print(f"Produto mais barato: {precoMin}")
        print(f"Produto mais caro: {precoMax}")
        break

    except ValueError:
        print("O valor não é um numero inteiro")