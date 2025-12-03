#Leia um caractere e informe se ele é letra maiúscula, minúscula, dígito ou outro símbolo.

while True:
    
    letra = str(input("Digite um caractere: "))

    if len(list(letra)) == 1:
        try:
            int(letra)
            print("Dígito")

        except ValueError:
            if not letra.isalnum():
                print("Caracter especial")
            elif letra == letra.lower():
                print("Letra minuscula")
            elif letra == letra.upper():
                print("Letra Maiuscula")
    else:
        print("Não foi digitado somente um caractere")
        

    