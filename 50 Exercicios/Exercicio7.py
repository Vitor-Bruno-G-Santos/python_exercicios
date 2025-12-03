#Leia o nome de um usuário e a senha, compare com valores pré-definidos e informe se o acesso deve ser permitido ou negado.
senhaPadrao = "Senha123"
loginPadrao = "Vitor"
acesso = 0
while True:
    login = str(input("Digite o seu usuário: "))
    senha = str(input("Digite a sua senha: "))
    
    if login == loginPadrao and senha == senhaPadrao:
        print("Acesso permitido")
        break
    else: 
        if acesso <2:
            acesso +=1
        else:
            print("Acesso negado\nChegou ao limite de tentativas")
            break
        print(f"Acesso negado\nMáximo 3 tentativas\nTentativa atual: {acesso}")
