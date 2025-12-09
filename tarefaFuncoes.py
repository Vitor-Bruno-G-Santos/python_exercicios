def notasAlunos():
    try:
        quantNotas = int(input("Digite quantas notas este aluno possui: "))
        notas = []
        for i in range(quantNotas):
            notas.append(float(input(f"Digite a {i + 1}º nota: ")))     
        return notas
    except ValueError:
        print("O numero digitado não é um numero ou não é um numero inteiro")
def mediaNota(notas : list):
    try:
        total = 0
        for i in notas:
            total += i
        return total / len(notas)
    
    except ValueError:
        print("Os recebidas não são somente numeros")
    except IndexError:
        print("A variavel recebida não é uma lista de notas")

def classificaAluno(media : float):
    if media >= 6:
        return "Aprovado"
    elif media < 6 and media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"
def Main():
    notas = notasAlunos()
    media = mediaNota(notas)
    classificacao = classificaAluno(media)
    print(f"Notas: {notas}\nMédia: {media}\nSituação: {classificacao}")

Main()