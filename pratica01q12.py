def converter():
    escala = input("Digite a escala desejada|C - Celsius|F - Fahrenheit|: ").upper()
    temperatura = int(input("Digite a temperatura a ser convertida: "))
    if escala == "C":
        