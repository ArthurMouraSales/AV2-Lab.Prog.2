#Questão 6
def contador():
    vogais = "aeiou"
    total = 0

    for char in texto:
        if char in vogais:
            total += 1
        
    print(total)

texto = input("Digite sua frase ou palavra: ")
contador()


    