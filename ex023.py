num = int(input("Digite um numero inteiro: "))
print("""Escolha uma das opções:
      [1] converter para BINARIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL""")
opcao = int(input("sua opção"))
if opcao == 1: 
    print("{} convertido para BINARIO é {}".format(num,bin(num)))
elif opcao == 2: 
    print("{} convertido para OCTAL é {}".format(num,oct(num)))
elif opcao == 3: 
    print("{} convertido para HEXADECIMAL é {}".format(num,hex(num)))
print("Opção Invalida!")