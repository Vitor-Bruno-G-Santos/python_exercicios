salarioFixo = float(input("Digite o seu salario fixo: "))
valorVendas = float(input("Digite o valor de vendas: "))

print(f"Valor da comissão: {valorVendas * 0.04}\nSalario final: {salarioFixo + (valorVendas * 0.04)}")