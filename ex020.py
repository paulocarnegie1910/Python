n1= float(input("Digite a Primeira nota:"))
n2 = float(input("Digite a Segunda nota:"))
media = (n1+n2)/2
print("A media do aluno(a) é: {}".format(media))
if media < 6:
    print("Aluno REPROVADO!")
else:
    print("Aluno APROVADO!")