nome = str(input("Digite vosso nome: "))
if nome =="Trump":
    print("Agora as tarifas aumentam!")
elif nome == "Lula" or nome == "Sirigueijo":
    print("Uau seu nome é igual ao do molusco do mar")
elif nome in "Ana Claudia Jessica Juliana":
    print("Belo nome feminino")
else:
    print("Belo nome")

print("Tenha um otimo dia, {}.".format(nome))