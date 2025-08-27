n1= float(input("Digite a Primeira nota:"))
n2 = float(input("Digite a Segunda nota:"))
media = (n1+n2)/2
print("A media do aluno(a) é: {}".format(media))
if media < 5:
    print("Aluno REPROVADO!")
elif 7> media >= 5:
    print("Aluno de RECUPERAÇÃO")
else:
    print("Aluno APROVADO!")