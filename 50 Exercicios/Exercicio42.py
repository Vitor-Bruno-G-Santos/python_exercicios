#Leia uma expressão aritmética simples digitada como texto, avalie e exiba o resultado, tratando expressões inválidas.
total = 0
try:
    expressao = str(input("Digite a expressão: "))
    nums = expressao.split()
    for i,j in enumerate(nums):
        if not j.isalnum() and i != 0:
            match j:
                case "+":
                    total += int(nums[i+1])
                case "-":
                    total -= int(nums[i+1])
                case "*":
                    total *= int(nums[i+1])
                case "/":
                    total /= int(nums[i+1])
        elif  i == 0:
            total = int(j)
except IndexError:
    print()
print("Total =",total)
