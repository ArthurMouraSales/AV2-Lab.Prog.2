#Questão 13
def verificar_email():
    if "@" in email:
        print("Email Valido!")
    else:
        print("Email Invalido!")
    
email = input("Digite seu email: ")
verificar_email()
