#Questão 7
def fatorial(numero):
    if numero > 0:
        return numero * fatorial(numero - 1)
    else:   
        return 1     
        


numero = int(input("Digite um valor inteiro: "))

print(f"O fatorial do numero {numero} é {fatorial(numero)}")