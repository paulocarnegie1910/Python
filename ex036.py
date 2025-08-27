n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))
op = 0

while op != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair!""")
    op = int(input("Qual é sua opção?: "))
    if op == 1:
        soma= n1 + n2
        print("A soma dos numeros {} + {} é {}".format(n1,n2,soma))
    elif op == 2:
        mult = n1 * n2
        print("A multiplicação dos numeros {} + {} é {}".format(n1,n2,mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
print("Entre {} e {} o maior valor é {}".format(n1,n2,maior))
    elif opcao == 4:
        