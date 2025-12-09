#Leia um nome de arquivo informado pelo usuário e trate o caso de o arquivo não existir, exibindo uma mensagem adequada.

arquivosExistentes = ["Excel", "Word", "Powerpoint","Explorer"]
procura = str(input("Digite o arquivo que está buscando: "))

for i in arquivosExistentes:
    if i == procura:
        print("Arquivo encontrado: ", i)
    else:
        print("O arquivo não foi encontrado")