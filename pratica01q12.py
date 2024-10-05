#Questão 12
def converter():
    temperatura = int(input("Digite a temperatura a ser convertida: "))
    escala = input("Digite a escala da temperatura informada anteriormente |C - Celsius|F - Fahrenheit|: ").upper()
    if escala == "C":
        fahrenheit = (temperatura * 9/5) + 32
        print(f"A temperatura digita em Celsius é igual a {fahrenheit}°F")
    elif escala == "F":
        celsius = (temperatura - 32) * 5/9
        print(f"A temperatura digitada em fahrenheit é igual a {celsius}°C")
    else:
        raise ValueError("A unidade informada é invalida, siga as instruções passadas anteriormente")

converter()