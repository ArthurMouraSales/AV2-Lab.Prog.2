#Questão 10
def contador():
    palavras = texto.strip().split()
    return len(palavras)

texto = input("Digite seu texto: ")

print(f"Número de palavras: {contador()}")