casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o salario do comprador?"))
anos = int(input("quantos anos para pagar?"))
print (anos)
parcela = casa/(anos*12)
print ("Para pagar uma casa de R${} em {} anos".format (casa,anos))
print("A prestação sera de R${:.2f}".format(parcela))
minimo = salario * 0.3
if parcela < minimo:
    print("Emprestimo CONCEDIDO!")

else: print("Emprestimo NEGADO!")