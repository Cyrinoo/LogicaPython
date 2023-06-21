num1 = int(input("Digite um numero:"))
num2 = int(input("Digite um numero:"))
num3 = int(input("Digite um numero:"))
if num1 > num2 and num1 > num3:
    print(f"Apresenta o maior numero: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Apresenta o maior numero: {num2}")
else:   
    print(f"Apresenta o maior numero: {num3}")
if num1 < num2 and num1 < num3:
    print(f"Apresenta o menor numero: {num1}")
elif num2 < num1 and num2 < num3:
    print(f"Apresenta o maior numero: {num2}")
else:   
    print(f"Apresenta o menor numero: {num3}")
