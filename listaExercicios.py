#Exercicio 1

'''numeros = []
print(numeros)'''

#Exercicio 2

'''idades = [10, 20, 15, 35, 55]
print(idades)'''

#Exercicio 3 

'''nomes = ["Vitor", "Lucas", "Gustavo", "Felipe", "Mateus"]

print(nomes[0],"e", nomes[-1])'''

#Exercicio 4

'''numeros = []

for i in range(3):
    numeros.append(int(input("Digite um numero inteiro: ")))

print(numeros)
for i in range(3):
    print(numeros[i])'''

#Exercicios 5

'''vetor = [1, "A", 5.5, 25 ,6]

for i in range(5):
    vetor[i] = input("Digite algo desejado: ")

print(vetor)'''

#Exercicios 6

'''numero = 0

for i in range(5):
    numero += int(input("Digite um numero: "))

print(numero)'''

#Exercicios 7

'''numero = 0

for i in range(5):
    numero += float(input("Digite um numero: "))

print("Media: ", numero / 5)'''

#Exercicios 8

'''vetor = []

for i in range(5): 
    vetor.append(float(input("Digite um numero: ")))

print(vetor)'''

#Exercicios 9

'''vetor = []

for i in range(5):
    vetor.append(int(input("Digite um numero: ")))

for i in range(-1, -6, -1):
    print(vetor[i])'''

#Exercicio 10

'''vetor = [1, 33, 222, 54, 122]

for i in range(5):
    vetor[i] = vetor[i] * 2

print(vetor)'''

#Exercicios 11

nome = ["Vitor", "Arthus", "Lucas", "Felipe"]

saudações = ["Ohayo ", "Ola, ", "Good morning ", "Buenos dias "]

for i in range(4):
    print(saudações[i], nome[i])

#Exercicios 12

'''numeros = []
contagemPares = 0
for i in range(6):
    numeros.append(int(input("Digite um numeros inteiro: ")))
    if numeros[i] % 2 == 0:
        contagemPares += 1

print(contagemPares)'''

#Exercicios 13

'''numeros = []

for i in range(5):
    numeros.append(int(input("Digite um numero: ")))
    

print(min(numeros), "E", max(numeros))'''

#Exercicios 14

'''nomes = []
busca = ""
for i in range(5):
    nomes.append(str(input("Digite um nome: ")))

busca = str(input("Digite o nome que deseja buscar: "))
for i in range(5):
    if(busca == nomes[i]):
        print("Tem o nome na lista: ", nomes[i])'''

#Exercicios 15

'''numeros = []

for i in range(5):
    numeros.append(float(input("Digite um numero: ")))

for i in range(-1, -6, -1):
    print(numeros[i])'''