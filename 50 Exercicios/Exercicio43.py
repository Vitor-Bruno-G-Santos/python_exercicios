#Simule um sistema de login que exige que nome de usuário e senha não sejam vazios, repetindo a solicitação enquanto necessário.
while True:
    verificaLogin = "Vitor123"
    verificaSenha = "Vitor123"
    login = str(input("Digite o seu login: "))
    if login.replace(" ","") != "":
        senha = str(input("Digite sua senha: "))
        if senha.replace(" ","") != "":
            if verificaLogin == login and verificaSenha == senha:
                print("Logado com sucesso")
                break
            else: 
                print("Tente novamente")
        else:
            print("A senha não pode estar vazia")
    else:
        print("O login não pode estar vazio")