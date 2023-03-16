#teste de importação
from exercicio import teste
# print(teste)

#EXERCICIO_(1)
# – Imprima as seguintes mensagens na tela (substitua o X e o Y pelo
# resultado da operação indicada na mensagem): 
# a = float(input("Digite um número:"))
# b = int(input("Digite um número:"))
# # • “A multiplicado por B é X”
# mult = a*b
# print("A multiplicado por B é %.2f"%mult)
# # • “A dividido por B é X”
# div = a/b
# print("A divisão por B é %.2f"%div)
# # • “A mais B é X e A menos B é Y”
# aMoreb = a+b
# aLessb = a-b
# print("A mais B é%.2f"%aMoreb,"e A menos B é %.2f"%aLessb)
# # • “A elevado a B é X” 
# elev = a**b
# print("A elevado a B é %.2f"%elev)

#EXERCICIO_(2)
# a = int(input("Digite um número (a):"))
# b = int(input("Digite um número (b):"))
# c = int(input("Digite um número (c):"))
a = 2
b = -5
c = 2

x1 = 0
x2 = 0

delta = (b**2)-(4*a*2)
x1 = (-b + (delta ** 0.5)) / (2*a)
x2 = (-b - (delta ** 0.5)) / (2*a)
print(x2)

#GABARITO#########################################

#EXERCICIO_(1)
# a = float(input("Digite o valor de a:"))
# b = int(input("Digite o valor de b:"))

# print("\nA multiplicado por B é",a*b,"...")
# print("A dividido por B é",a/b,", mas com duas casas decimais é %.2f" % (a/b),"!")
# print("A mais B é",a+b," e A menos B é",a-b)
# print("A elevado a B é",a**b) 
#EXERCICIO_(2)
# a = int(input("Digite o valor de a: "))
# b = int(input("Digite o valor de b: "))
# c = int(input("Digite o valor de c: "))

# xLinha = ( (b * -1) + (b**2 - 4 * a * c) ** (1/2) ) / (2 * a)
# xDuasLinhas = ( (b * -1) - (b**2 - 4 * a * c) ** (1/2) ) / (2 * a)

# print("***** Raizes da equação *****")
# print("x' =",xLinha)
# print("x'' =",xDuasLinhas)
