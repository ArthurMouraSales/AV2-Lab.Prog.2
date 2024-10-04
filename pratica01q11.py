#Questão 11
def media():
    lista = []

    num = int(input("Digite a quantidade de numeros a ser digitado: "))
    while len(lista) != num:
        lista.append(int(input("Digite um numero: ")))

    soma = sum(lista)
    calculo = soma / len(lista)
    print(f"{calculo}")

media()