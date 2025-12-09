#Crie um menu com as opções: cadastrar usuário, listar usuários, remover usuário e sair. Trate cada opção com seleção múltipla.

while True:
    try:
        opt = int(input("1 - Cadastrar usuario\n2 - Listar usuarios\n3 - Remover usuario\n0 - Sair\nDigite a opção desejada: "))

        match opt:
            case 1:
                print("Cadastro de usuario")
                input("Aperte enter para voltar")
            case 2:
                print("Listando usuarios")
                input("Aperte enter para voltar")
            case 3:
                print("Pode remover um usuario")
                input("Aperte enter para voltar")
            case 0:
                print("Saindo")
                break
    except ValueError:
        print("A opção digitada não é um numero inteiro")