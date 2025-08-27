from datetime import date
atual = date.today().year
nasc = int(input("Digite o ano de nascimento: "))
idade = atual - nasc
if idade == 18:
    print("voc/~e tem que se alistar imediatament")
elif idade <18:
    saldo = 18-idade
    print("ainda faltam {} anos para o alistamento".format(saldo))
    ano = atual + saldo
    print("seu alistamento será em {} anos". format(saldo))

elif idade >18:
    saldo = idade - 18
    print("voce deveria ter se alistado há {} anos".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))