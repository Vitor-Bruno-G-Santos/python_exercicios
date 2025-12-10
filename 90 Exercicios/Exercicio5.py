#Faça um algoritmo que leia o nome do aluno, o nome da disciplina, notas de 3 provas e calcule a média desse aluno. Posteriormente imprima o resultado de cada variável linha abaixo de linha.

nome = str(input("Digite seu nome: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3
print(nome,'\n', media)