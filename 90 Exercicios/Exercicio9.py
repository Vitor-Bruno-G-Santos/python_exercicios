nomeAluno = str(input("Digite o nome do aluno: "))
disciplina = str(input("Qual a disciplina: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

print(nomeAluno, disciplina, nota1, nota2, nota3, media)