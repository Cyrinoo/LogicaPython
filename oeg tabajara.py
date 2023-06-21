sal = int(input("Digite o salário:"))
sal1 = (sal * 0.20)
sal2= (sal * 0.15)
sal3= (sal * 0.10)
sal4= (sal * 0.5)
salf1 = (sal + sal1)
salf2 = (sal + sal2)
salf3 = (sal + sal3)
salf4 = (sal + sal4)

if  sal <= 280:
    print(f"o seu salario antes era {sal} e agora sera: {salf1}")
elif sal >= (280 and 700 * 0.15):
    print(f"o seu salario antes era {sal} e agora sera: {salf2}")
elif sal >= (700 and 1500 * 0.10):
    print(f"o seu salario antes era {sal} e agora sera: {salf3}")
elif sal <= (1500 * 0.5):
    print(f"o seu salario antes era {sal} e agora sera: {salf4}")
