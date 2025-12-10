#Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre o valor da comissão e o salário final do funcionário

salarioFixo = float(input("Digite o seu salario fixo: "))
valorVendas = float(input("Digite o valor de vendas: "))

print(f"Valor da comissão: {valorVendas * 0.04}\nSalario final: {salarioFixo + (valorVendas * 0.04)}")