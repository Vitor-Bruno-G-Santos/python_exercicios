#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva: F - Feminino, M – Masculino ou Sexo Inválido.

sexo = str(input("Digite o seu sexo: F - feminino, M - Masculino "))

if (sexo == 'M'):
    print("Masculino")
elif (sexo == "F"):
    print("Feminino")
else:
    print("Sexo invalido")