#Leia uma string representando um e-mail e determine se ela possui o formato básico de um endereço eletrônico.
valido = False
while valido == False:
    naoUse = " !#$%^&*()+="
    dominios = ["hotmail.com.br", "hotmail.com", "gmail.com"]
    email = str(input("Digite o seu email (obs: pode ser hotmail ou gmail): "))
    if any(especial in email for especial in naoUse):
        print("Email contem caracteres invalidos\nExemplo ' ', '!', '#', '$', '%', '^', '&', '*', '(', ')', '+', '='")
    elif email[0] == "." or email[-1] == ".":
        print("Não pode ter ponto no inicio nem no fim")
    elif len(email) > 320:
        print("Email invalido")
    else:
        for i, j in enumerate(email):
            if j == "." and email[i + 1] == ".":
                print("Não pode ter 2 pontos seguidos")
                break
            else:
                if "@" in email:
                    if j == "@":
                        if i >64:
                           print("Email invalido")
                        elif email[i + 1:len(email)] in dominios:
                            print("Email valido")
                            valido = True
                            break
                        else:
                            print("Email invalido")
                            break
                else:
                    print("Email invalido")
                    break