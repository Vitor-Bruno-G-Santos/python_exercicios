salario = float(input("Digite o salario: "))
salarioPos = 0
percentual = 0
valorAumento = 0

if salario <= 280:
    percentual = 0.2
    valorAumento = salario * percentual
    salarioPos = salario + valorAumento
elif salario <= 700:
    percentual = 0.15
    valorAumento = salario * percentual
    salarioPos = salario + valorAumento
elif salario <= 1500:
    percentual = 0.1
    valorAumento = salario * percentual
    salarioPos = salario + valorAumento
else:
    percentual = 0.05
    valorAumento = salario * percentual
    salarioPos = salario + valorAumento

print(salario)
print(percentual)
print(valorAumento)
print(salarioPos)