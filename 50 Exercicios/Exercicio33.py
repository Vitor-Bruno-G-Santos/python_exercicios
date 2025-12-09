#Leia uma sigla de estado civil (S, C, D, V) e exiba o estado civil correspondente, ou informe se for inválido.

while True:
    estadoCivil = str(input("S - Solteiro\nC - Casado\nD - Divorciado\nV - Viuvo\nDigite o estado civil correspondente: ")).upper()
    match estadoCivil:
        case "S":
            print("Voce está solteiro(a)")
            break
        case "C":
            print("Voce esta casado(a)")
            break
        case "D":
            print("Voce esta divorciado(a)")
            break
        case "V":
            print("Voce é viuvo(a)")
            break
        case _:
            print("Opção invalida")
            input("Aperte ENTER para voltar")