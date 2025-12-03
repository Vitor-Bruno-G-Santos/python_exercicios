#Leia uma string representando um e-mail e determine se ela possui o formato básico de um endereço eletrônico.
while True:
    valido = True
    naoUse = " !#$%^&*()+="
    dominios = ["hotmail.com.br", "hotmail.com", "gmail.com", "gmail.com.br", "@"]
    email = str(input("Digite o seu email (obs: pode ser hotmail ou gmail): "))
    if any(especial in email for especial in naoUse):
        print("Email contem caracteres invalidos\nExemplo ' ', '!', '#', '$', '%', '^', '&', '*', '(', ')', '+', '='")
    else:
        for i, j in enumerate(email):
            
            if j == "@":
                for dom in dominios:
                    if email[i + 1:len(email)] == dom:
                        print("Certo")
                        break
                    else:
                        print('Dominio incorreto\nDominios aceitos: "hotmail.com.br", "hotmail.com", "gmail.com", "gmail.com.br"')
                        break
            if valido == False:
                print("Email invalido")
            

    