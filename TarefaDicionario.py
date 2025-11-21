biblioteca = []

opt = 1
while opt != 0:
    opt = int(input("1 - Cadastrar livro\n2 - Buscar por nome\n3 - Buscar por autor\n4 - Buscar por gênero\n5 - Listar todos\n6 - Marcar como lido\n0 - Sair\nDigite a opção desejada: "))
    match opt:
        case 1:
            if len(biblioteca) == 100:
                print("Biblioteca cheia")
            else:
                nome = str(input("Digite o nome do livro: "))
                autor = str(input("Digite o nome do autor(a): "))
                genero = str(input("Digite o gênero do livro: "))
                ano = str(input("Digite o ano em que o livro foi escrito: "))
                status = int(input("1 - Lido\n2 - Não lido\nDigite a opcão correspondente: "))
                leu = "Lido" if status == 1 else "Não lido"
                biblioteca.append({"NOME": nome,
                                   "AUTOR": autor,
                                    "GENERO": genero,
                                    "ANO": ano,
                                    "STATUS": leu})
        case 2:
            nome = str(input("Digite o nome do livro: "))
            for i,j in enumerate(biblioteca):
                if j.get("NOME") == nome:
                    print(biblioteca[i])
        case 3:
            livros = []
            autor = str(input("Digite o autor do livro: "))
            for i,j in enumerate(biblioteca):
                if j.get("AUTOR") == autor:
                    livros.append(i)
            if livros != None:
                print("Encontrei estes livros do autor: ", autor)
                j = 1
                for i in range(len(livros)):
                    print(j," - ", biblioteca[livros[i]].get("NOME"))
                    j += 1
            else:
                print("Não encotrei livros deste autor")
            livroDesejado = int(input("Digite o numero livro desejado conforme os mostrados acima: "))
            print("\n\n\n")
            print(biblioteca[livroDesejado - 1])
            
            input()
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
        case 4:
            genero = str(input("Digite o genero do livro: "))
            for i,j in enumerate(biblioteca):
                if j.get("GENERO") == genero:
                    print(biblioteca[i])

