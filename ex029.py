preco = float(input("valor das compras: R$"))
print('''FORMAS DE PAGAMENTO
      [1]à vista dinheiro/cheque
      [2]à vista cartão
      [3]2x no cartão
      [4]3x oumais no cartão''')
opcao = int(input("Qual a opção? "))
if opcao == 1:
    total= preco - (preco*0.1)
elif opcao == 2:
    total = preco - (preco*5/100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print("Sua compra será parcelada em 2X de {:.2f}".format(parcela))
elif opcao == 4:
    total = preco + (preco *0.2)
    totalparc = int(input("Quantas vezes: "))
    parcela = total/totalparc
    print("Sua compra parcelada em {} de R$ {:.2f} com juros".format(totalparc,parcela))
else:
    print("ERRO! Escolha uma das opçoes validas")
    
print("Sua compra R${} vai custar R${} no valor final".format(preco,total))