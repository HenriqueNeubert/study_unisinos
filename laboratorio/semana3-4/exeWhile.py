#EXERCICIO_(1)
# Crie um programa que pede para o usuário digitar o nome de 13 pessoas
# pelo teclado.

# i = 1

# while i <= 13:
#   name = str(input(f"Digite um nome ({i}/13):"))
#   i += 1

#EXERCICIO_(2)
# Crie um programa que imprime os números de 0 a 1000.

# i = 0
# while i <= 1000:
#   print(i)
#   i += 1

#EXERCICIO_(3)
# . Crie um programa que imprime os números pares de 0 a 2000.

# i = 0
# while i <= 1000:
#   print(i)
#   i += 2

#EXERCICIO_(4)
# . . Crie um programa que imprime os números de 0 a 1000 em ordem
# decrescente (ou seja, de 1000 a 0).

# i = 1000
# while i >= 0:
#   print(i)
#   i -= 2

#EXERCICIO_(5)
#   Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final,
# imprima quantos torcedores torcem para o Grêmio

# i = 1
# gremio = 0
# while i <= 5:
#   time = str(input(f"Digite o nome de um clube ({i}/5):"))
#   if time == "Gremio" or time == "gremio" or time == "GREMIO":
#     gremio = gremio + 1
#   i+= 1
# print(gremio)

#EXERCICIO_(6)
# Crie um programa que pede para o usuário digitar 20 números com ponto
# flutuante pelo teclado. Ao final, seu programa deve imprimir todos os números
# digitados. Dica: armazene-os em uma string e concatene os valores digitados. 
# No final,imprima a string.

# i = 1
# listNumber = []
# while i <= 3:
#   number = float(input(f"Digite um número ({i}/3):"))
#   listNumber.append(number)
#   i+= 1
# print(listNumber)

#CORREÇÃO
# i = 1
# listNumber = ""
# while i <= 3:
#   number = float(input(f"Digite um número ({i}/3):"))
#   listNumber = listNumber + str(number)+ "\n"
#   i+= 1
# print(listNumber)
#CORREÇÃO

#EXERCICIO_(7)
# Crie um programa que solicita para o usuário que ele digite 10 valores
# inteiros. Ao final, imprima a soma de todos os valores digitados.

# i = 1
# number = 0
# soma = 0
# while i <= 10:
#   number = int(input(f"Digite um valor ({i}/10):"))
#   soma = soma + number
#   i += 1
# print(soma)

#EXERCICIO_(8)
# Crie um programa que pergunta para o usuário (via Teclado) quantos
# números ele irá digitar e armazena em uma variável chamada quant. Logo após, 
# faça com que o usuário digite quant números inteiros, e para cada número 
# digitado imprima na tela se o número é negativo, positivo ou zero.

# quant = int(input("Quantidade de números que serão digitados:"))
# i = 1
# while i <= quant:
#   number = int(input(f"Digite o número ({i}/{quant}):"))
#   if number == 0:
#     print("O número é zero")
#   elif number > 0:
#     print(number, "é positivo.")
#   else:
#     print(number, "é negativo.")
#   i += 1 

#EXERCICIO_(9)
# Crie um programa que pede para o usuário digitar 2 valores inteiros via
# Teclado (val1 e val2). Se nenhum dos valores for negativo, escreva os números 
# pares entre o menor e o maior valor.

# val1 = int(input("Digite um valor:"))
# val2 = int(input("Digite um valor:"))

# if val1 > val2:
#   while val2 <= val1:
#     print(val2)
#     val2 += 2
# elif val2 > val1:
#   while val1 <= val2:
#     print(val1)
#     val1 += 2

# if val1 or val2 < 0:
#   print("ERRO!!!\nUm dos valores é negativo.")

#EXERCICIO_(10)
# Crie um programa que faça a soma dos valores de 0 até 198.

# i = 0
# soma = 0
# while i <= 198:
#   soma = soma + i
#   i += 1 
# print(soma)

#EXERCICIO_(11)
# Crie um programa que imprima a soma dos valores pares e a soma dos
# valores ímpares entre dois números quaisquer digitados pelo usuário

###ESTUDAR###

# valor1 = 2
# valor2 = 6

# somaPares = 0
# somaImpares = 0

# if valor1 < valor2:
#   cont = valor1
#   while cont < valor2:
#     if cont % 2 == 0:
#       somaPares += cont
#     else:
#       somaImpares += cont
#     cont += 1
# else:
#   print("[ERRO] Valor1 >= Valor2")

#EXERCICIO_(12)
#  Crie um programa que pede para o usuário digitar números positivos via
# Teclado. Quando o usuário digitar um número negativo, informe a média de 
# todos os números que ele informou.

# start = 1
# i = 0
# soma = 0
# while start:
#   number = int(input("Digite números positivos:"))
#   if number < 0:
#     print(soma)
#     break
#   else:
#     soma = soma + number 
#     i += 1

#EXERCICIO_(13)
# Crie um programa que calcule o fatorial de um número informado pelo
# usuário (não permita números negativos).

#ESTUDAR
# number = int(input("Digite um número:"))
# fatorial = 1
# count = number
# i = 1

# if number == 0:
#   print("!!!ERRO!!!\nNúmero não pode ser zero.")
# else:
#   while count > 1:
#     fatorial = fatorial * count
#     count -= 1
#   print(fatorial) 
#ESTUDAR

#EXERCICIO_(14)
# Crie um programa que diga se o número informado pelo usuário é primo
# ou não

#ESTUDAR
# num = int(input("Digite um valor inteiro: "))
# isPrimo = True
# cont = 2
# while cont < num:
#   if num % cont == 0:
#     isPrimo = False
#     break
#   cont += 1

# if isPrimo:
#   print("� primo!")
# else:
#   print("N�o � primo!")
#ESTUDAR

#EXERCICIO_(15)
# Crie um programa que imprime os números primos entre 0 e 200,
# imprimindo ao final a soma destes números.