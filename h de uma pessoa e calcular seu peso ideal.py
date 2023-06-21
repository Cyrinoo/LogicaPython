print("programa para calcular altura")
alt = float( input("Digite o sua altura: "))
sx = input("Digite o seu sexo: ")
sxmas = (72.7 * alt) - 58
sxfem = (62.1 *alt) - 44.7
if sx == "masculino":
    print("Seu peso como macho ideal é:",sxmas, "kg")
else:
    print("Seu peso como femea ideal é:",sxfem, "kg")
