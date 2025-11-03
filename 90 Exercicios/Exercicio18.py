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