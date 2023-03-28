#EXERCICIO_(1)
# . Crie um programa que pede para o usuário digitar o nome de 13 pessoas
# pelo teclado.

# for i in range(0, 13):
#   name = input("Digite seu nome:")

#EXERCICIO_(2)
# Crie um programa que imprime os números de 0 a 1000.

# for i in range(0, 1001):
#   print(i)

#EXERCICIO_(3)
# Crie um programa que imprime os números pares de 0 a 2000.

# for i in range(0, 2001, 2):
#   print(i)

#EXERCICIO_(4)
# Crie um programa que imprime os números de 0 a 1000 em ordem
# decrescente (ou seja, de 1000 a 0).
# lista = range(1001, 0, -1)
# for i in lista:
#   print(i)

#EXERCICIO_(5)
#Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final,
#imprima quantos torcedores torcem para o Grêmio.

# count = 0
# for i in range(0, 11):
#   clube = input("Digite o nome do clube:")
#   if clube == "gremio":
#     count += 1
# print("Um total de ", count, "pessoas torcem para o Grêmio.")

#EXERCICIO_(6)
#Crie um programa que pede para o usuário digitar 20 números com ponto
#flutuante pelo teclado. Ao final, seu programa deve imprimir todos os números
#digitados. Dica: armazene-os em uma string e concatene os valores digitados. 
# No final, imprima a string.

# lista = ""
# for i in range(0, 3):
#   number = float(input("Digite um número:"))
#   lista += str(number) + "\n"
# print(lista)

#EXERCICIO_(7)
# Crie um programa que solicita para o usuário que ele digite 10 valores
# inteiros. Ao final, imprima a soma de todos os valores digitados.

# soma = 0
# for i in range(0, 5):
#   number = int(input("Digite um número:"))
#   soma += number
# print(soma)

#EXERCICIO_(8)
# Crie um programa que pergunta para o usuário (via Teclado) quantos
# números ele irá digitar e armazena em uma variável chamada quant. Logo após,
# faça com que o usuário digite quant números inteiros, e para cada número 
# digitado imprima na tela se o número é negativo, positivo ou zero.

# quant = int(input("Quantidade:"))

# for i in range(0, quant):
#   number = int(input("Digite um número:"))
#   if number == 0:
#     print("Zero", number)
#   elif number < 0:
#     print("Negativo", number)
#   else:
#     print("Positivo", number)

#EXERCICIO_(9)
# Crie um programa que pede para o usuário digitar 2 valores inteiros via
# Teclado (val1 e val2). Se nenhum dos valores for negativo, escreva os números 
# pares entre o menor e o maior valor.

# val1 = int(input("Digite um número:"))
# val2 = int(input("Digite um número:"))

# if val1 != 0 and val2 != 0:
#   if val1 != val2:
#     if val1 < val2:
#       for i in range(val1, val2):
#          if i % 2 == 0:
#            print(i)
#     else:
#       for i in range(val2, val1):
#         if i % 2 == 0:
#           print(i)

#EXERCICIO_(10)
# Crie um programa que faça a soma dos valores de 0 até 198.

# count = 0
# for i in range(0, 199):
#   count += i
# print(count)

#EXERCICIO_(11)
# Crie um programa que imprima a soma dos valores pares e a soma dos
# valores ímpares entre dois números quaisquer digitados pelo usuário.

# val1 = int(input("Digite um número:"))
# val2 = int(input("Digite um número:"))

# pares = 0
# impares = 0
# for i in range(val1, val2 + 1):
#   if i % 2 == 0:
#     pares += i
#   else:
#     impares += i
# print(pares)
# print(impares)

#EXERCICIO_(12)
# Crie um programa que pede para o usuário digitar números positivos via
# Teclado. Quando o usuário digitar um número negativo, informe a média de todos 
# os números que ele informou.

#EXERCICIO_(13)
# Crie um programa que calcule o fatorial de um número informado pelo
# usuário (não permita números negativos).

# number = int(input("Digite um número:"))
# count = 5

# if number > 0:
#   for i in range(1, number):
#     count = count * i
# print(count)

#EXERCICIO_(14)
# Crie um programa que diga se o número informado pelo usuário é primo
# ou não

# #ESTUDAR
# num = int(input("Digite um número:"))

# isPrimo = True
# cont = 2
# while cont < num:
#   if num % cont == 0:
#     isPrimo = False
#     break
#   cont += 1

# if isPrimo:
#   print("é primo!")
# else:
#   print("Não é primo!")
#ESTUDAR

#ESTUDAR
#EXERCICIO_(15)
# Crie um programa que imprime os números primos entre 0 e 200,
# imprimindo ao final a soma destes números.
#ESTUDAR