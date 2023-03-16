#EXERCICIO_(1-A)
#crie um algoritmo que solicita o nome do usuário pelo teclado e imprime na tela este nome
'''
name = input("Digite seu nome:")
print("Seu nome é", name)
'''
#EXERCICIO_(1-B)
#crie um algoritmo que pede o nome e a idade de dois jogadores (um de cada vez).
#  Ao final, imprima o nome do jogador mais velho
'''
namePlayer1 = input("Digite seu nome:")
agePlayer1 = int(input("Digite sua idade: (1)"))

namePlayer2 = input("Digite seu nome:")
agePlayer2 = int(input("Digite sua idade: (2)"))

if agePlayer1 > agePlayer2:
  print("Player",namePlayer1,"é mais velho")
if agePlayer2 > agePlayer1:
  print("Player",namePlayer2,"é mais velho")
if agePlayer1 == agePlayer2:
  print("Ambos os jogadores tem:", agePlayer1, "anos")
'''
#EXERCICIO_(1-C)
# crie um algoritmo que solicita o nome do usuário e a idade dele pelo teclado.
#  O algoritmo deve imprimir na tela uma das mensagens abaixo:
# “Você é adulto”, quando a idade digitada for maior ou igual a 18 --
# “Você é adolescente”, quando a idade digitada for menor do que 18 e maior do que 13--
# “Você é criança”, quando a idade digitada for maior ou igual a 0 e menor ou igual a 13--
# “Idade inválida”, quando a idade digitada for menor do que 0
# name = input("Digite seu nome:")
# age = int(input("Digite sua idade:"))
# if age >= 18:
#   print("Você é adulto")
# elif age < 18 and age > 13:
#   print("Você é um adolescente")
# elif age >= 0 and age <= 13:
#   print("Você é uma criança")
# elif age < 0:
#   print("Idade inválida")

#EXERCICIO_(1-D)
# crie um algoritmo que lê 4 números do teclado e imprime na tela se a soma dos
#  4 números é um valor par ou ímpar
# n1 = int(input("Digite um número(1/4):"))
# n2 = int(input("Digite um número(2/4):"))
# n3 = int(input("Digite um número(3/4):"))
# n4 = int(input("Digite um número(4/4):"))
# total = n1 + n2 + n3 + n4
# if total >= 0:
#   print("Positivo")
# else:
#   print("Negativo")

#EXERCICIO_(1-E)
# crie um algoritmo que solicita que o usuário digite 10 números pelo teclado e,
#  a cada número digitado, imprima na tela se o número é positivo, negativo ou zero
n1 = int(input("Digite um número(1/10):"))
if n1 >= 0:
  print("Positivo")
else:
  print("Negativo")

#EXERCICIO_(8)
'''
n1 = float(input("Digite um número?"))
n2 = float(input("Digite um número?"))

total = n1 / n2
print("%.2f" % total)
print("%.3f" % total)
print("%.4f" % total)
'''
