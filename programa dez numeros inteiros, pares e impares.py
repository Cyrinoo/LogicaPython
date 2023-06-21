for controle in range(10):
    numero = int(input("Digite os numeros: "))
    if (numero % 2) != 0:
        totalImpares = totalImpares + 1
    else:
        totalPares = totalPares + 1
    print(f"O total de numeros pares é de: {totalPares}")
    print(f"O total de numeros impares é de: {totalImpares}")
