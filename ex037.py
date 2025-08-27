import random
numero_secreto = random.randint(1,10)
tentativas = 0
max_tentativas = 3
print("-----------Jogo da Adivinhação-------------")
print("Estou pensando em um numero entre 1 e 10. voce tem {} tentativas".format(max_tentativas))
while tentativas < max_tentativas:
    chute = int(input("Qual seu palpite?: "))
    tentativas +=1
    if chute == numero_secreto:
        print("Parabens! voce acertou o numero {} em {} tentativas".format(numero_secreto,tentativas))
    elif chute < numero_secreto:
        print("Muito Baixo! tente um numro maior")
    else:
        print("Muito Alto! Tente um numero menor")
    # verifica o numero de tentativas
    if tentativas < max_tentativas:
        print("Tentativas restantes: {}".format(max_tentativas))
    else:
        print("Suas tentativas acabaram!")
        print("O numero secreto era: {}".format(numero_secreto))