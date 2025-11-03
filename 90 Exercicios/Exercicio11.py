nome = str(input("Qual seu nome: "))
idade = int(input("Qual sua idade: "))
tipo = ""

if(idade >= 0 and idade <= 2):
    tipo = "Bebê"
elif(idade >= 3 and idade <= 11):
    tipo = "Criança"
elif(idade >= 12  and idade <= 21):
    tipo = "Jovem"
elif(idade >= 22 and idade <= 64):
    tipo = "Adulto"
elif(idade >= 65 and idade <= 100):
    tipo = "Idoso"
else:
    tipo = "Muito velinho"

print(nome, "está com", idade, "e pela tabela é considerado", tipo)