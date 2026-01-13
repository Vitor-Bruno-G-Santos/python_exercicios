def notasAlunos():
    try:
        quantNotas = int(input("Digite quantas notas este aluno possui: "))
        notas = []
        i = 0
        
        while i < quantNotas:
            notaDigitada = float(input(f"Digite a {i + 1}º nota: "))
            if notaDigitada <= 10 and notaDigitada >= 0:
                notas.append(notaDigitada)    
                i += 1
            else: 
                print("As notas devem ser de 0 a 10")

        return notas, quantNotas
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
    while True:
        try:
            notas = notasAlunos()
            media = mediaNota(notas)
            classificacao = classificaAluno(media)
            print(f"Notas: {notas}\nMédia: {media}\nSituação: {classificacao}")
            break
        except:
            print("Ocorreu um erro")

Main()