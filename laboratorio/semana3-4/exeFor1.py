#EXERCICIO_(1)
# . Crie um programa imprime na tela os valores de 1 a 100 (incluindo o 1 e o
# 100).

# for i in range(1, 101):
#   print(i)

#EXERCICIO_(2)
# . Crie um programa que imprime na tela todos os valores entre dois valores
# digitados pelo teclado.

# numberA = int(input("Digite um número:"))
# numberB = int(input("Digite um número:"))

# for i in range(numberA, numberB):
#   print(i)

#EXERCICIO_(3)
# Crie um programa que imprime a tabuada de um número qualquer digitado
# pelo usuário.

# number = int(input("Digite um número:"))

# for i in range(1,11):
#   print(i, "X", number, "=", i*number)

#EXERCICIO_(4)
# Sabendo que uma string é uma lista de letras, peça para o usuário digitar
# um texto e imprima na tela a quantidade de vogais que existem no texto.

# text = str(input("Digite uma palavra:"))
# count = 0
# for i in text:
#   if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#     count += 1
# print("Nesta palavra existem", count, "vogais.")

#EXERCICIO_(5)
# Crie um programa que permita que o usuário crie sua lista de compras.
# Primeiramente, solicite que ele informe quantos produtos serão adicionados
# na lista. Depois disto, peça para que o usuário digite os produtos que ele 
# vai comprar, e armazene em uma lista. Ao final, imprima a lista de compras
# do usuário.

# quant = int(input("DIGITE A QUANTIDADE DE PRODUTOS:"))
# lista = []

# for i in range(1, quant + 1):
#   item = input(f"Digite o item ({i}/{quant}):")
#   lista.append(item)
# print("---LISTA COMPLETA---")
# for i in lista:
#   print("Item:", i)
# print("---LISTA COMPLETA---")

#EXERCICIO_(6)
# Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo
# teclado. Ao final, imprima apenas o nome das pessoas separadas por estado civil:
# solteiras, casadas, divorciadas e viúvas (nesta ordem!)

# solteiro = []
# casadas = []
# divorciadas = []
# viuvas = []
# for i in range(1, 21):
#   name = input(f"Digite seu nome ({i}/20):")
#   status = input(f"Digite seu estado civil ({i}/20):")
#   if status == "solteiro":
#     solteiro.append(name)
#   elif status == "casadas":
#     casadas.append(name)
#   elif status == "divorciadas":
#     divorciadas.append(name)
#   elif status == "viuvas":
#     viuvas.append(name)
#   else:
#     print("Inválido")

# print("---SOLTEIROS---")
# for i in solteiro:
#   print(i)
  
# print("---CASADOS---")
# for i in casadas:
#   print(i)

# print("---DIVORCIADOS---")
# for i in divorciadas:
#   print(i)

# print("---VIOVOS---")
# for i in viuvas:
#   print(i)

#EXERCICIO_(7)
# Crie um programa que solicita ao usuário que ele defina sua senha. A senha
# deve ser um texto (string) composto apenas por dígitos e deve ter entre 5 e 10
# valores.O usuário tem apenas 6 chances de definir corretamente a senha. Caso 
# ele defina corretamente a senha nas tentativas que ele tem, imprima uma 
# mensagem de sucesso.Caso ele não defina a senha corretamente, imprima uma 
# mensagem de insucesso. Dica:na aula aprendemos a ver se uma string é formada 
# apenas por dígitos e aprendemos a descobrir o tamanho do texto digitado.

# definir senha 5-10 , apenas 6 chances + msg sucesso
# se não msg erro

# acertou = False
# for i in range(0,6):
#   senha = input("Defina a senha:")
#   if senha.isdigit() and len(senha) >= 5 and len(senha) <= 10:
#     print("!!!SENHA CADASTRADA COM SUCESSO!!!")
#     acertou = True
#     break
#   else:
#     print("!!!Senha inválida!!!")
# if(not(acertou)):
#   print("Quantidade de tentativas excedida!")

#EXERCICIO_(8)
#Crie um programa que separa o joio do trigo. Seu programa deve ler a lista
#abaixo e criar duas listas diferentes: uma com todas as ocorrências da palavra 
#"joio" e outra com todas as ocorrências da palavra "trigo". Ao final, 
#imprima as listas separadas.Copie e cole a linha abaixo no seu código e 
#complete o programa:

# joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo",
# "joio", "joio", "joio", "joio", "trigo", "trigo", "joio",
# "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo",
# "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
# "joio", "joio", "joio", "joio", "joio", "joio", "joio",
# "joio", "trigo", "trigo", "joio", "joio", "joio", "joio",
# "joio", "joio", "joio", "joio", "joio", "joio", "joio",
# "joio", "joio", "joio", "joio", "joio", "trigo", "trigo",
# "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
# "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
# "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio",
# "joio", "joio", "joio", "joio", "joio", "joio", "joio",
# "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
# "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio",
# "joio", "joio", "trigo", "joio", "joio", "joio", "joio",
# "joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio",
# "joio", "joio", "joio", "joio", "joio", "trigo", "trigo",
# "trigo", "joio", "trigo", "joio", "joio", "joio"]

# joio = []
# trigo = []

# for i in joioETrigo:
#   if i == "joio":
#     joio.append(i)
#   else:
#     trigo.append(i)

# print(joio)
# print(trigo)

#EXERCICIO_(9)
# Faça novamente todos os exercícios das listas de exercícios sobre WHILE,
# porém utilizando o for para realizar a repetição.