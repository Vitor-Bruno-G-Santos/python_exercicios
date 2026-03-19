def buscaBinaria(lista: list, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return chute
        if chute > item:
            print("loop1")
            alto = meio - 1
        else:
            baixo = meio + 1
            print("loop2")
    return None

listaTest = [1,2,3,4,5,6,7,8,9]

print(buscaBinaria(listaTest, 4))