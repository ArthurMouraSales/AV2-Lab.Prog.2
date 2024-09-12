def calculadora():
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite outro valor"))
    print("Para a proxima pergunta utilize |A - Adição|S - Subtração|M - Multiplicação|D - Divisão|")
    operacao = input("Qual operação você quer realizar? ").upper()
    if operacao == "A":
        adicao = num1 + num2
        print(f"{adicao}")
    elif operacao == "S":
        sub = num1 - num2
        print(f"{sub}")
    elif operacao == "M":
        mult = num1 * num2
        print(f"{mult}")
    elif operacao == "D":
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

