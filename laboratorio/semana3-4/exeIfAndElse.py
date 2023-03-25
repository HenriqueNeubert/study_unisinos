#EXERCICIO_(1)
# . Crie um programa que recebe um inteiro pelo teclado e imprime se ele é
# par ou ímpar.
# number = int(input("Digite um número:"))

# if number % 2 == 0:
#   print("PAR")
# else:
#   print("IMPAR")

#EXERCICIO_(2)
# . Crie um programa que recebe dois valores inteiros pelo teclado e imprime
# qual dos dois é maior.
# numberA = int(input("Digite um número:"))
# numberB = int(input("Digite um número:"))

# if numberA > numberB:
#   print("O número maior é:", numberA)
# elif numberA == numberB:
#   print("Os números são iguais")
# else:
#   print("O número maior é:", numberB)

#EXERCICIO_(3)
# . Crie um programa que recebe dois valores inteiros A e B pelo teclado e
# imprime o valor de A dividido por B. Entretanto, se o valor de B for 0, imprima uma
# mensagem de erro e não faça a divisão

# numberA = int(input("Digite um número:"))
# numberB = int(input("Digite um número:"))

# if numberB != 0:
#   print("O resultado é:", numberA / numberB)
# else:
#   print("O segundo número é zero:")

#EXERCICIO_(4)
# . Crie um programa que recebe três valores inteiros pelo teclado e imprime
# qual dos três é menor.

# def criada apenas para fins de conhecimento
# def mensagem(texto, param):
#   print(texto, param)

# numberA = int(input("Digite um número (A):"))
# numberB = int(input("Digite um número (B):"))
# numberC = int(input("Digite um número (C):"))

# if numberA < numberB and numberA < numberC:
#   mensagem("O menor número é (A):", numberA)
# elif numberB < numberA and numberB < numberC:
#   mensagem("O menor número é (B):", numberB)
# else:
#   mensagem("O menor número é (C):", numberC)

#EXERCICIO_(5)
# . Crie um programa que recebe o preço de um produto pelo teclado e
# imprime na tela a mensagem adequada, de acordo com o preço:
# • “Preço inválido”, se o preço for negativo ou zero
# • “Preço baixo”, se o preço for entre 0 e 30 (inclusive)
# • “Preço médio”, se o preço for entre 30 e 50 (inclusive)
# • “Preço alto”, se o preço for maior do que 50

# def message(text, var):
#   print(text, var)

# price = float(input("Digite o valor do produto:"))

# if price <= 0: 
#   message("!!!ERRO!!!\nO preço é zero ou negativo.\n Preço digitado: R$%.2f" % price)
# elif price <= 30 and price >= 0:
#   message("!!!PREÇO BAIXO!!!\nO preço digitado está abaixo do limite de R$ 30,00.\n Preço digitado: R$%.2f" % price)
# elif price <= 50 and price >=31:
#   message("!!!PREÇO MÉDIO!!!\nO preço digitado está em nossa média entre R$ 31,00 e R$50,00.\n Preço digitado: R$%.2f" % price)
# elif price >= 50:
#   message("!!!PREÇO ALTO!!!\nO preço digitado está ultrapassando nosso limite de R$50,00.\n Preço digitado: R$", price)

#EXERCICIO_(6)
# Crie um programa que aplica uma taxa de juros em um determinado preço
# digitado pelo teclado. A taxa aplicada deve ser:
# • Aumento de 10% caso o valor seja menor do que 100
# • Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
# • Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
# • Imprima uma mensagem de erro se o valor for negativo
# • Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.

# price = float(input("Digite o valor do produto:"))

# if price < 100 and price > 0:
#   print("Valor Total:", price, "\nTotal c/juros (10%): R$", price * 0.1 + price)    
# elif price >= 100 and price <= 300:
#   print("Valor Total:", price, "\nTotal c/juros (20%): R$", price * 0.2 + price)    
# elif price >= 301 and price <= 1000:
#   print("Valor Total:", price, "\nTotal c/juros (50%): R$", price * 0.5 + price)    
# elif price <= 0:
#   print("Valor negativo: \n R$", price)

#EXERCICIO_(7)
#  Crie um programa que recebe um valor inteiro referente a um
# determinado ano. Imprima na tela se o ano informado é bissexto ou não.

# year = int(input("Digite o ano:"))

# if year % 4 == 0:
#   print("O ano é bissexto.")
# else:
#   print("O ano não é bissexto.")

#EXERCICIO_(8)
# . Crie um programa que exibe um menu de calculadora na tela. O menu
# exibido deve ser o seguinte:
# • Digite 1 para somar dois valores
# • Digite 2 para subtrair dois valores
# • Digite 3 para multiplicar dois valores
# • Digite 4 para dividir dois valores
# • Digite 5 para realizar uma potência entre dois valores
# • Digite 6 para realizar uma radiciação entre dois valores
# • Digite qualquer outro número para sair
# De acordo com a opção informada pelo usuário, solicite os valores necessários para o
# usuário e imprima na tela o resultado da operação realizada.

# print("Digite 1 para somar dois valores")
# print("Digite 2 para subtrair dois valores")
# print("Digite 3 para multiplicar dois valores")
# print("Digite 4 para dividir dois valores")
# print("Digite 5 para realizar uma potência entre dois valores")
# print("Digite 6 para realizar uma radiciação entre dois valores")
# print("Digite qualquer outro número para sair")
# print("//////////////////////////////////////////////////////////")

# digito = int(input("Digite o número:"))

# if digito == 1:
#   valorA = int(input("Digite o número:"))
#   valorB = int(input("Digite o número:"))
#   print("A soma de", valorA, "+", valorB, "é:", valorA + valorB)
# elif digito ==2:
#   valorA = int(input("Digite o número:"))
#   valorB = int(input("Digite o número:"))
#   print("A subtração de", valorA, "-", valorB, "é:", valorA - valorB)
# elif digito ==3:
#   valorA = int(input("Digite o número:"))
#   valorB = int(input("Digite o número:"))
#   print("A multiplicação de", valorA, "*", valorB, "é:", valorA * valorB)
# elif digito ==4:
#   valorA = int(input("Digite o número:"))
#   valorB = int(input("Digite o número:"))
#   print("A divisão de", valorA, "/", valorB, "é:", valorA / valorB)
# elif digito ==5:
#   valorA = int(input("Digite o número:"))
#   valorB = int(input("Digite o número:"))
#   print("A potênciação de", valorA, "por", valorB, "é:", valorA ** valorB)
# elif digito ==6:
#   valorA = float(input("Digite o número:"))
#   valorB = float(input("Digite o número:"))
#   print("A radiação de", valorA, "por", valorB, "é:", (valorA**(1/valorB)))
# else:
#   print("SAIU")

#EXERCICIO_(9)
# Crie um programa que recebe a nota do Grau A e a nota do Grau
# B pelo teclado e imprime na tela se será necessário ou não realizar o Grau C
# (considere o sistema de avaliação da Unisinos). Caso algum valor informado
# seja negativo, informe uma mensagem de erro e não realize o cálculo.

#grau-a = 30
grauA = float(input("Digite sua nota (GRAU-A)"))
#grau-b = 70
grauB = float(input("Digite sua nota (GRAU-B)"))

#
#
#