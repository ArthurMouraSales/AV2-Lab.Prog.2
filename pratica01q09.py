#Questão 9
def soma():
    lista = []
    while len(lista) != numero:
        lista.append(int(input("Digite um numero: ")))
    soma = sum(lista)
    print(f"{soma}")


numero = int(input("Digite a quantidade de numeros a ser digitado: "))
soma()