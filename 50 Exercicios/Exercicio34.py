#Simule um caixa de lanchonete que leia o código de um produto, a quantidade e exiba o nome do item e o valor total.

produtos = [{"CODIGO": 1,"PRODUTO":"Cachorro quente",  "PRECO": 8},
            {"CODIGO":2,"PRODUTO":"Coca-cola","PRECO":4},
            {"CODIGO": 3,"PRODUTO":"Pepsi", "PRECO": 3}]
produtosComprados = []
total = 0
while True:
    try:

        opt = int(input("0-Sair\nDigite o codigo do produto: "))
        if opt == 0:
            break
        else:
            produtosComprados.append(produtos[opt-1])
            total += produtos[opt-1].get("PRECO")
    except ValueError:
        print("O valor digitado não é um numero inteiro")
for i in produtosComprados:
    print(f"Codigo: {i.get("CODIGO")} -- Produto: {i.get("PRODUTO")} -- Preço: {i.get("PRECO")}")

print(f"Total: {total}")