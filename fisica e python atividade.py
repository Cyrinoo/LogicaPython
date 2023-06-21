opcao = 1
while opcao != 0:
    print("Digite 0 para sair: ")
    print("Digite 1 para Velocidade")
    print("Digite 2 para Empuxo")
    print("Digite 3 para Movimento Uniforme ")
    print("Digite 4 para Peso ")
    print("Digite 5 para Segunda Lei de Newton ")
    print("Digite 6 para Equação dos pontos conjugados ")
    print("Digite 7 para Velocidade de Ondas ")
    print("Digite 8 para Força ")
    print("Digite 9 para Potência elétrica")
    print("Digite 10 para equação de Torricelli")
    print("Digite 11 para Quantidade de Movimento")
    print("Digite 12 para Termodinamica")
    print("Digite 13 para Trabalho ")
    print("Digite 14 para Primeira Lei de Ohm")
    print("Digite 15 para Segunda Lei de Ohm")

    opcao = int(input("Digite uma das opções: "))
    if opcao == 1:

        Vo = float(input("Digite a Velocidade Inicial m/s: "))
        acl = float(input("Digite a aceleração:"))
        temp = float(input("Digite o valor do tempo: "))
        Vdv = (Vo + acl * temp )
        print(f"A velocidade é igual a: {Vdv}")

    elif opcao == 2:

        Df = float(input("Digite a Densidadade Do Fluido: "))
        Vi = float(input("Digite o valor do Volume Imerso de um corpo no fluido:"))
        Gravi = float(input("Digite a aceleração de gravidade: "))
        VdE = ( Df * Vi * Gravi )
        print(f"O empuxo é igual a: {VdE}")

    elif opcao == 3:

        So = float(input("Digite a opção inicial movel: "))
        Velo = float(input("Digite a velocidade:"))
        tmp = float(input("Digite o valor do tempo: "))
        VdMU = (So + Velo * tmp )
        print(f"O movimento uniforme é igual a: {VdMU}")

    elif opcao == 4:

        Mass = float(input("Digite a Massa: "))
        Gravid = float(input("Digite a Gravidade:"))
        Peso = (Mass * Gravid )
        print(f"O Peso é igual a: {Peso}")

    elif opcao == 5:

        Mdc = float(input("Digite a Massa do corpo: "))
        Acle = float(input("Digite a Aceleração:"))
        Fr = (Mdc * Acle )
        print(f"A força resultante é igual a: {Fr}")

    elif opcao == 6:

        DdoE = float(input("Digite a  Distancia do Objeto ao Espelho: "))
        DdiE = float(input("Digite a  Distancia da imagem ao Espelho:"))
        Fdee = (1/DdoE + 1/DdiE)
        print(f"A equação é igual a: {Fdee}")

    elif opcao == 7:

        QnO = float(input("Digite o comprimento da onda em m/s: "))
        FdO = float(input("Digite a Frequencia da onda em Hz:"))
        VdO = (QnO * FdO)
        print(f"A velocidade é igual a: {VdO}")

    elif opcao == 8:

        mass1 = float(input("Digite a massa: "))
        acl1 = float(input("Digite a Aceleração:"))
        aF = (mass1 * acl1)
        print(f"A força é igual a: {aF}")

    elif opcao == 9:

        Dpo = float(input("Digite a diferença de potencial: "))
        coele = float(input("Digite a corrente elétrica:"))
        Pe = (Dpo * coele)
        print(f"A potencia eletrica é igual a: {Pe}")

    elif opcao == 10:

        Veloini = float(input("Digite a velocidade inicial: "))
        Acele = float(input("Digite a aceleração:"))
        Ds = float(input("Digite o espaço percorrido pelo corpo:"))
        Prt1 = (Veloini**2 + 2 * Acele * Ds)
        ResFin = (Prt1**2)
        print(f"A equação é igual a: {ResFin}")

    elif opcao == 11:

        mass3 = float(input("Digite a massa em kg: "))
        velo1 = float(input("Digite a velocidade:"))
        QdM = (velo1 * mass3)
        print(f"A quantidade de movimento é igual a: {QdM}")

    elif opcao == 12:

        Qdd = float(input("Digite Quantidade de calor: "))
        Tbl = float(input("Digite o Trabalho:"))
        TdA = (Qdd - Tbl)
        print(f"A Termodinâmica é igual a: {TdA}")        

    elif opcao == 13:

        Fra = float(input("Digite a força: "))
        Desl = float(input("Digite o Deslocamento:"))
        Trb = (Fra * Desl)
        print(f"A formula do trabalho é igual a: {Trb}")

    elif opcao == 14:

        Dpot = float(input("Digite a diferença de potencial: "))
        IdC = float(input("Digite a intensidade de corrente eletrica:"))
        rc = (Fra * Desl)
        print(f"A resistência constante é igual a: {rc}")

    elif opcao == 15:

        RedoCo = float(input("Digite resistividade do condutor: "))
        Compr = float(input("Digite o comprimento:"))
        Adst = float(input("Digite o valor da área de secção transversal: "))
        res1 = (RedoCo * Compr)
        Resfinal = (res1/Adst)
        print(f"A a resistência elétrica de um material é diretamente proporcional ao seu comprimento que é igual a: {Resfinal}")