#Questão 3
def calculadora():
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite outro valor: "))

    adicao = num1 + num2
    print(f"{adicao}")
    
    subtracao = num1 - num2
    print(f"{subtracao}")
    
    multiplicacao = num1 * num2
    print(f"{multiplicacao}")
    
    if num2 == 0:
        print("Não é possivel dividir por 0")
    # Se não for, sera realizado o calculo da divisão
    else:
        divisao = num1 / num2
        print(f"{divisao}")
    # Se a resposta não for igual a nenhuma das possibilades acima sera exibido uma mensagem de erro
   
calculadora()