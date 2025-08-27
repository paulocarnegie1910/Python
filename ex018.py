a = int(input("1º numero:"))
b = int(input("2º numero:"))
c = int(input("3º numero:"))
#começar procurando o menor valor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#O maior valor
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("O menor valor digitado foi: {}".format(menor))
print("O maior valor digitado foi: {}".format(maior))