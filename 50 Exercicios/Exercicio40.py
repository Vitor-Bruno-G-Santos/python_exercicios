#Leia nome e idade de várias pessoas até que o usuário decida encerrar. Desconsidere idades inválidas

idades = []

while True:
    try:

        valor = int(input("Digite a idade ou 0 para sair: "))
        if valor == 0:
            break
        else:
            idades.append(valor)
    
    except ValueError:
        print("O valor digitado não é um numero inteiro")
print(idades)