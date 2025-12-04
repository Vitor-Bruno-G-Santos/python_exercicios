#Gere e exiba os 20 primeiros termos da sequência de Fibonacci.
n0 = 1
n1 = 1
print(n0)
for i in range(19):
    print(n0)
    temp = n0
    n0 += n1
    n1 = temp
