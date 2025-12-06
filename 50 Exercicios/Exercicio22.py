# Leia uma senha e continue pedindo-a até que o usuário digite a senha correta, informando ao final quantas tentativas foram realizadas.
senha = "vitor123"
tentativas = 0
while True:
    try:
        
        senhaDigitada = str(input("Digite a sua senha: "))
        if senha == senhaDigitada:
            print("Senha correta")
            tentativas += 1
            break
        else:
            print("Senha incorreta")
            tentativas +=1
    
    except ValueError:
        print("O que foi digitado não é aceito como senha")
print("Quantidade de tentativas:", tentativas)