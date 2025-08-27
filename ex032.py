somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho =""
mulhernova = 0
for p in range(1,5):
    print("----------{}ª Pessoa---------".format(p))
    nome = str(input("Nome: ".strip() )) # remove os espaços do nome
    idade = int(input("Idade: "))
    sexo = str(input("Genero [M/F]: ".strip() ))
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        mulhernova += 1


mediaidade = somaidade/4
print("A media de idade do grupo é {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem,nomevelho))
print("Existem {} mulheres com menos de 20 anos".format(mulhernova))