login = str("paulo")
senha = int(1234)
tentativas = 0
max_tentativas = 3
while tentativas < max_tentativas:
    user = str(input("Login: "))
    passw = int(input("Senha: "))
    if user == login and passw == senha:
        print("Login bem sucedido!")
        break
    elif user != login or passw != senha:
        print("usuario ou Senha incorretos")
        tentativas +=1
        print("voce tem {} tentativas restantes.".format(tentativas))
if tentativas >= 3:
    print("Tentativas esgotadas")