p1 = int( input("Digite o primeiro preço: "))
p2 = int(input("Digite o segundo preço: "))
p3 = int(input("Digite o terceiro preço: "))

if p1 < p2:
    print(f"Esse produto de {p1} que devará comprar porque é mais barato")
elif p1 < p3:
    print(f"Esse produto de {p1} que devará comprar porque é mais barato")
elif p2 < p1:
    print(f"Esse produto de {p2} que devará comprar porque é mais barato")
elif p2 < p3:
    print(f"Esse produto de {p2} que devará comprar porque é mais barato")
elif p3 < p1:
    print(f"Esse produto de {p3} que devará comprar porque é mais barato")
elif p3 < p2:
    print(f"Esse produto de {p3} que devará comprar porque é mais barato")
