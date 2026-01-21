tamanho = int(input("Digite o tamanho da tabuada: "))
matriz = []
for i in range(0,tamanho + 1):
    matriz.append([i])
    for j in range(1,tamanho + 1):
        if i > 0:
            matriz[i].append(j * i)
        else:
            matriz[i].append(j)

for i in range(len(matriz)):
    print(matriz[i])