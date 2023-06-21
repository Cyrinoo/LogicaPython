n1 = int( input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
seq = n1, n2, n3
resultado = sorted(seq, reverse=True)
print(resultado)
