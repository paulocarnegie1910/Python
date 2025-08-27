from random import randint
itens = ("Pedra","Papel","Tesoura")
computador = randint(0,2)
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input("Qual a sua jogada? "))
print("-=-"*15)
print("COMPUTADOR jogou {}".format(itens[computador]))
print("JOGADOR jogou {}".format(itens[jogador]))
print("-=-"*15)
if jogador == computador:
    print("EMPATE")
elif jogador > computador:
    print("JOGADOR GANHOU")
elif jogador > computador:
    print("COMPUTADOR GANHOU")
else:
    print("NÃO PERMITIDO")