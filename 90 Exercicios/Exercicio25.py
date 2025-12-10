'''Uma fábrica de camisetas produz os tamanhos pequeno,
médio e grande, cada uma sendo vendida respectivamente por
R$10,00, R$12,00 e R$15,00. Faça um algoritmo em que o
usuário forneça a quantidade de camisetas pequenas, médias e
grandes referentes a uma venda, o algoritmo informe qual o valor
total da compra.'''

while True:
    try:

        camisetaP = int(input("Digite a quantidade de camisetas pequenas: "))
        camisetaM = int(input("Digite a quantidade de camisetas medias: "))
        camisetaG = int(input("Digite a quantidade de camisetas grandes: "))
        total = (camisetaP * 10) + (camisetaM * 12) + (camisetaG * 15)
        print(f"Total: {total}")
        break

    except ValueError:
        print("O valor digitado não é um número inteiro")