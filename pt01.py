# Criando uma função para a calculadora
def calculadora():
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite outro valor: "))
    print("Para a proxima pergunta utilize |A - Adição|S - Subtração|M - Multiplicação|D - Divisão|")
    operacao = input("Qual operação você quer realizar? ").upper()
    # Se a resposta for (A) ira realizar a adição dos numeros digitados
    if operacao == "A":
        adicao = num1 + num2
        print(f"{adicao}")
    # Se a resposta for (S) ira realizar a subtração dos numeros digitados
    elif operacao == "S":
        sub = num1 - num2
        print(f"{sub}")
    # Se a resposta for (M) ira realizar a multiplicação dos numeros digitados
    elif operacao == "M":
        mult = num1 * num2
        print(f"{mult}")
    # Se a resposta for (D) ira realizar a divisão dos numeros digitados
    elif operacao == "D":
        # Porem se o segundo numero digitado for 0, sera exibido uma mensagem de erro, ja que não é possivel dividir nenhum valor por 0
        if num2 == 0:
            print("Não é possivel dividir por 0")
        # Se não for, sera realizado o calculo da divisão
        else:
            div = num1 / num2
            print(f"{div}")
    # Se a resposta não for igual a nenhuma das possibilades acima sera exibido uma mensagem de erro
    else:
        print("Erro na digitação da operação")
while True:
    calculadora()
    resp = input("Deseja realizar mais alguma operação |S - Sim|N - Não|? ").upper()
    if resp == "S":
        calculadora()
    else:
        break
