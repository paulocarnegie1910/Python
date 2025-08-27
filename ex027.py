from datetime import date
atual = date.today().year
nascimento =  int(input("Ano de nascimento: "))
#descobrir idade, sempre atual primeiro depois nascimento
idade = atual - nascimento
print("O Atleta tem {} anos".format(idade))
if idade <= 9: 
    print("Mirim")
elif idade <=14:
    print("Infantil")
elif idade <=19:
    print("Junior")
elif idade <=25:
    print("Senior")
else:
    print("Master")