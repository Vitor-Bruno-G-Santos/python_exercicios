#Leia duas notas e a quantidade de faltas de um aluno e determine sua situação escolar considerando média e frequência.

while True:
   try:

      nota1 = float(input("Digite a primeira nota: "))
      nota2 = float(input("Digite a segunda nota: "))
      faltas = int(input("Digite a quantidade de faltas: "))
      aulas = int(input("Digite a quantidade de aulas: "))
      media = (nota1 + nota2) / 2
      porFalta = 100 - ((faltas / aulas) * 100)

      print(f"Media = {media:.1f}\nPercentual de falta = {porFalta:.0f}")
      if media > 6 and porFalta > 25:
         print("Aprovado")
         break
      else:
         if porFalta > 0:
            print("Reprovado")
            break
         else:
            print("As faltas foram informadas a mais que a quantidade de aula")

   except ValueError:
      print("Valor invalido")
