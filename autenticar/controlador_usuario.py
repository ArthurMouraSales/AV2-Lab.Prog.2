#Questão 5
usuarios = [
    {
        "username": "teste",
        "password": "admin"
    },
    {
        "username": "teste2",
        "password": "admin2" 
    },
    {
        "username": "teste3",
        "password": "admin3" 
    },
    {
        "username": "teste4",
        "password": "admin4" 
    },
]
def login():
    username = input("Digite seu username: ")
    password = input("Digite sua senha: ")

    for login in usuarios:
        if login['username'] == username and login['password'] == password:
            print("Acesso Liberado")
            return 1
        else:
            print("Acesso negado")
            return 1

login()