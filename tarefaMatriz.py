#1.CRIE UM PROGRAMA QUE LEIA VALORES INTEIROS PARA PREENCHER UMA MATRIZ 2 × 2.DEPOIS DE PREENCHIDA, MOSTRE A MATRIZ NA TELA ORGANIZADA EM LINHAS E COLUNAS.

'''
matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um numero inteiro: ")))
    matriz.append(linha)
for i in matriz:
    print(i)
'''
#2.CRIE UMA MATRIZ 3 × 3 JÁ PREENCHIDA COM NÚMEROS INTEIROS DEFINIDOS NO CÓDIGO.MOSTRE TODOS OS VALORES DA MATRIZ NA TELA, LINHA POR LINHA.
'''
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in matriz:
    print(i)
'''
#3.CRIE UM PROGRAMA QUE PERGUNTE AO USUÁRIO O NÚMERO DE LINHAS E COLUNAS DE UMA MATRIZ.EM SEGUIDA, LEIA OS VALORES E MOSTRE A MATRIZ FORMADA.
'''
linha = int(input("Digite a quantidade de linhas: "))
coluna = int(input("Digite a quantidade de colunas: "))
matriz = []
for i in range(linha):
    linha = []
    for i in range(coluna):
        linha.append(int(input("Digite um numero inteiro: ")))
    matriz.append(linha)
for i in matriz:
    print(i)
'''
#4.CRIE DUAS MATRIZES 2 × 2 COM VALORES INFORMADOS PELO USUÁRIO.GERE UMA TERCEIRA MATRIZ CONTENDO A SOMA DAS DUAS MATRIZES E MOSTRE O RESULTADO.
'''
matriz1 = []
matriz2 = []
matriz3 = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um numero inteiro: ")))
    matriz1.append(linha)
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um numero inteiro: ")))
    matriz2.append(linha)
for i in range(2):
    linha =[]
    for j in range(2):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(linha)
for i in matriz3:
    print(i)
'''
#5.CRIE DUAS MATRIZES 3 × 3 COM VALORES INTEIROS.CALCULE E MOSTRE A MATRIZ RESULTANTE DA SOMA, SOMANDO OS VALORES QUE ESTÃO NA MESMA POSIÇÃO.
'''
matriz1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz2 = [
    [10,11,12],
    [13,14,15],
    [16,17,18]
]
matriz3 = []

for i in range(3):
    linha =[]
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(linha)
for i in matriz3:
    print(i)
'''
#6.CRIE DUAS MATRIZES 2 × 3 PREENCHIDAS PELO USUÁRIO. UTILIZE LAÇOS DE REPETIÇÃO PARA GERAR UMA TERCEIRA MATRIZ COM A SOMA DAS DUAS.
'''
matriz1 = []
matriz2 = []
matriz3 = []
for i in range(2):
    linha =[]
    for j in range(3):
        linha.append(int(input("Digite um numero inteiro: ")))
    matriz1.append(linha)
for i in range(2):
    linha =[]
    for j in range(3):
        linha.append(int(input("Digite um numero inteiro: ")))
    matriz2.append(linha)
for i in range(2):
    linha =[]
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(linha)
for i in matriz3:
    print(i)        
'''

#7.CRIE UMA MATRIZ 2 × 2 E UM NÚMERO INTEIRO.MULTIPLIQUE TODOS OS VALORES DA MATRIZ POR ESSE NÚMERO E MOSTRE A NOVA MATRIZ.

'''
matriz1 = []
matriz2 = []
numero = int(input("Digite um numero inteiro: "))
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um numero inteiro para a matriz: ")))
    matriz1.append(linha)
    matriz2.append(linha)

print(matriz1)
for i in range(2):
    for j in range(2):
        matriz2[i][j] = matriz2[i][j]* numero
    print(matriz2[i])
print(matriz1)
'''

#8. CRIE DUAS MATRIZES 2 × 2 COM VALORES INTEIROS. CALCULE A MULTIPLICAÇÃO ENTRE ELAS E MOSTRE A MATRIZ RESULTANTE.
'''
matriz1 = [
    [1,2],
    [3,4]
]
matriz2 = [
    [5,6],
    [7,8]
]
matrix = []
for i in range(len(matriz1)):
    linha = []
    for j in range(len(matriz1)):
        num = 0
        for k in range(len(matriz1)):
            num += matriz1[i][k] * matriz2[k][j]
        linha.append(num)
    matrix.append(linha)
print(matrix)
'''

#9. CRIE DUAS MATRIZES COMPATÍVEIS PARA MULTIPLICAÇÃO (2 × 3 E 3 × 2). CALCULE E MOSTRE A MATRIZ RESULTANTE DA MULTIPLICAÇÃO.

'''
matriz1 = [
    [1,2,3],
    [5,6,7]
]
matriz2 = [
    [8,9],
    [10,11],
    [12,13]
]
matrix = []
for i in range(2):
    linha = []
    for j in range(2):
        num = 0
        for k in range(3):
            num += matriz1[i][k] * matriz2[k][j]
        linha.append(num)
    matrix.append(linha)
print(matrix)
'''
#10. CRIE UMA MATRIZ QUE REPRESENTE A QUANTIDADE DE PRODUTOS VENDIDOS (2 × 2) E OUTRA MATRIZ QUE REPRESENTE O PREÇO DESSES PRODUTOS (2 × 2). UTILIZE A MULTIPLICAÇÃO DE MATRIZES PARA GERAR UMA MATRIZ QUE REPRESENTE O VALOR TOTAL DAS VENDAS.
'''
matriz1 = []
matriz2 = []

for i in range(2):
    linha =[]
    for j in range(2):
        linha.append(int(input("Digite a quantidade de produtos vendidos: ")))
    matriz1.append(linha)
for i in range(2):
    linha =[]
    for j in range(2):
        linha.append(int(input("Digite o valor dos produtos: ")))
    matriz2.append(linha)
matrix = []
for i in range(2):
    linha = []
    for j in range(2):
        num = 0
        for k in range(2):
            num += matriz1[i][k] * matriz2[k][j]
        linha.append(num)
    matrix.append(linha)
print(matrix)'''