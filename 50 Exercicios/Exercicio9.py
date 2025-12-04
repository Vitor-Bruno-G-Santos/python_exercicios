#Leia o salário bruto de um funcionário e calcule o salário líquido com base em regras de desconto por faixa salarial.

while True:
    try:
        salarioBruto = float(input("Digite o valor do salário bruto: "))

        if salarioBruto < 1518:
            print(f"Salario liquido = {print}")

    except ValueError:
        print("Valor digitado não é um numero")
