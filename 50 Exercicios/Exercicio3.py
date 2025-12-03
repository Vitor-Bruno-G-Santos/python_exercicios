#Leia a nota final de um aluno e classifique-o como aprovado, recuperação ou reprovado, conforme a faixa de valores permitida.
try:
    nota = float(input("Digite a nota: "))

    print("Aprovado" if nota >= 6 else "Reprovado")

except ValueError:
    print("Valor invalido")