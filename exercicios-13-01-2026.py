#EXERCICIO 1

aluno = {}

aluno["NOME"] = input("Digite o nome do aluno: ")
aluno["IDADE"] = input("Digite a idade do aluno: ")
aluno["CURSO"] = input("Digite o curso em que o aluno está matriculado: ")
for i in aluno:
    print(f"{i}: {aluno[i]}")

#EXERCICIO 2

produto = {"NOME":"ARROZ", "PREÇO":"50","QUANTIDADE":"5"}
print("Digite qual informação do produto deseja buscar: ")

while True:
    for i,j in enumerate(produto):
        print(f"{i + 1} - {j}")
    opt = int(input())
    if opt <= 3 and opt >= 1:
        break
    else:
        print("Opção invalida")
for i,j in enumerate(produto):
    if opt == i + 1:
        print(produto[j])

    