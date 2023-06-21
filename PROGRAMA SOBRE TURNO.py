tn = input("Digite o seu turno (M para Matutino, V para Vespertino e N de Noturno): ")
if tn == "M" or "m":
    print("Bom dia")
elif tn == "V" or "v":
    print("Boa Tarde")
elif tn == "N" or "n":
    print("Boa Noite")
else:
    print("Valor Invalido")
