#Leia o salário bruto de um funcionário e calcule o salário líquido com base em regras de desconto por faixa salarial.

while True:
    try:
        
        salarioBruto = float(input("Digite o valor do salário bruto: "))

        if salarioBruto < 1518 and salarioBruto > 0:
            print(f"Salario liquido = {salarioBruto - (salarioBruto * 0.075)}")
            break
        elif salarioBruto >= 1518 and salarioBruto < 2793:
            print(f"Salario liquido = {salarioBruto - (salarioBruto * 0.075) - (salarioBruto * 0.09)}")
            break
        elif salarioBruto >= 2793 and salarioBruto < 4190:
            print(f"Salario liquido = {salarioBruto - (salarioBruto * 0.15) - (salarioBruto * 0.12)}")
            break
        elif salarioBruto >= 4190:
            print(f"Salario liquido = {salarioBruto - (salarioBruto * 0.14) - (salarioBruto * 0.225)}")
            break
        else:
            print("O salario não pode ser zero ou menor")


    except ValueError:
        print("Valor digitado não é um numero")
