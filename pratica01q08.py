#Questão 8
def primo():
    divizoes = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divizoes.append(i)
    if divizoes[0] == 1 and divizoes[1] == numero:
        print(f"O {numero} é primo")
        
    else:
        print(f"O {numero} não é primo")

numero = int(input("Digite um numero: "))
primo()
        