#Leia as vendas diárias de uma semana e exiba o total, a média, o maior e o menor valor, além da lista ordenada
vendas = []
total = 0
for i in range(0,7):
    match i:
        case 0:
            vendas.append(float(input("Digite as vendas de segunda: ")))
        case 1:
            vendas.append(float(input("Digite as vendas de terça: ")))
        case 2:
            vendas.append(float(input("Digite as vendas de quarta: ")))
        case 3:
            vendas.append(float(input("Digite as vendas de quinta: ")))
        case 4:
            vendas.append(float(input("Digite as vendas de sexta: ")))
        case 5:
            vendas.append(float(input("Digite as vendas de sabado: ")))
        case 6:
            vendas.append(float(input("Digite as vendas de domingo: ")))
    total += vendas[i]
vendas.sort()
print(f"Total de vendas = {total}\nMédia de vendas = {total / len(vendas)}\nMenor venda = {min(vendas)}\nMaior venda = {max(vendas)}\nVendas = {vendas}")