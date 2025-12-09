# Leia cinco notas e armazene em uma lista. Exiba as notas, a média e as notas acima da média.


while True:
    try:
        notas = []
        notasAcima = []
        media = 0
        for i in range(5):
            notas.append(float(input(f"Digite a {i + 1}º nota:")))
            media += notas[i]
            
        media =  media / len(notas)
        for i in enumerate(notas):
            print(f"{i[0] + 1}º Nota: {i[1]}")
            if i[1] >= media:
                notasAcima.append(i[1])
        
        for i in enumerate(notasAcima):
            print(f"{i[0] + 1} Nota acima da media: {i[1]}")
        print(f"Média: {media}")
        break


    except ValueError:
        print("O que foi digitado não é um numero")