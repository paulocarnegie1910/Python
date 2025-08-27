genero = str(input("Informe seu Gênero: [M/F]")).strip().upper()
while genero not in "MmFf":
    genero = str(input("Dados invalidos. Insira [M/F]: ")).strip().upper()
print("Genero {} registrato com sucesso".format(genero))