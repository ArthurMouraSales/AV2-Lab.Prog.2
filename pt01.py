while True:
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite outro valor"))
    resp = input("Qual operação você quer realizar? ")
    if resp == "adicao":
        adicao = num1 + num2
        print(f"{adicao}")
    elif resp == "subtracao":
        sub = num1 - num2
        print(f"{sub}")
    elif resp == "multiplicacao":
        mult = num1 * num2
        print(f"{mult}")
    elif resp == "divisao":
        if num2 == 0:
            print("Não é possivel dividir por 0")
        else:
            div = num1 / num2
            print(f"{div}")
    else:
        print("Erro na digitação da operação")

