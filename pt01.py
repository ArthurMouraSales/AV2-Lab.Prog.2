def calculadora():
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite outro valor"))
    operacao = input("Qual operação você quer realizar? ")
    if operacao == "adicao":
        adicao = num1 + num2
        print(f"{adicao}")
    elif operacao == "subtracao":
        sub = num1 - num2
        print(f"{sub}")
    elif operacao == "multiplicacao":
        mult = num1 * num2
        print(f"{mult}")
    elif operacao == "divisao":
        if num2 == 0:
            print("Não é possivel dividir por 0")
        else:
            div = num1 / num2
            print(f"{div}")
    else:
        print("Erro na digitação da operação")
while True:
    calculadora()
    resp = input("Deseja realizar mais alguma operação |S - Sim|N - Não|? ").upper()
    if resp == "S":
        calculadora()
    else:
        break

