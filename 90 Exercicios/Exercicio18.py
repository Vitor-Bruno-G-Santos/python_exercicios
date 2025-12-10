'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa
que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora
é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00'''

valorHora = float(input("Digite o valor da sua hora: "))
quantidadeHora = int(input("Digite o valor de horas trabalhadas: "))

salarioBruto = valorHora * quantidadeHora
fgtsPer = 11
irPer = 0
inssPer = 10
fgts = 0
ir = 0
inss = 0

if salarioBruto <= 900:
    inss = salarioBruto * (inssPer / 100)
    fgts = salarioBruto * (fgtsPer / 100)
    
elif salarioBruto <= 1500:
    irPer = 5
    ir = salarioBruto * (irPer / 100)
    inss = salarioBruto * (inssPer / 100)
    fgts = salarioBruto * (fgtsPer / 100)
elif salarioBruto <= 2500:
    irPer = 10
    ir = salarioBruto * (irPer / 100)
    inss = salarioBruto * (inssPer / 100)
    fgts = salarioBruto * (fgtsPer / 100)
else:
    irPer = 20
    ir = salarioBruto * (irPer / 100)
    inss = salarioBruto * (inssPer / 100)
    fgts = salarioBruto * (fgtsPer / 100)


print("Salario bruto:", salarioBruto,
      "\nIR(", irPer, "%): R$" , ir,
      "\nINSS(",inssPer,"%): R$", inss,
      "\nFGTS(",fgtsPer,"%): R$", fgts,
      "\nTotal de descontos: R$", inss + fgts + ir,
      "\nSalario Liquido: R$", salarioBruto - inss - fgts - ir 
      )