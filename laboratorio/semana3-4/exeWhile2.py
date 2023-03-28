#EXERCICIO_(1)

# number = int(input("Digitar número:"))

# if number < 0:
#   print("!Erro! Número negativo:", number)
# elif number == 0:
#   print("!Erro! Número número é zero:", number)
# else:
#   print("Número é:", number)

#EXERCICIO_(2)
# i = 0
# while i <= 1000:
#   print(i)
#   i += 1
  
#EXERCICIO_(3)

# num1 = int(input("Digite um número:"))
# num2 = int(input("Digite um número:"))

# if num1 > num2:
#   print("Erro!")
# else:
#   while num1 <= num2:
#     print(num1)
#     num1 += 1
    
#EXERCICIO_(4)

# num1 = int(input("Digite um número:"))
# num2 = int(input("Digite um número:"))

# if num1 > num2:
#   while num1 >= num2:
#     print(num2)
#     num2 += 1
# else:
#   while num1 <= num2:
#     print(num1)
#     num1 += 1

#EXERCICIO_(5)
# i = 1
# count = 0
# while i <= 1000:
#   print(i)
#   count += i 
#   i += 1 
# print(count)

#EXERCICIO_(6)
# positivo 
# # par
# i = 1
# while i <= 10:
#   number = int(input("Digite um número que seja positivo e par:"))
#   if number < 0:
#     print("ERRO!!! \nNúmero negativo")
#   elif number % 2 == 0:
#     print("Você digitou:", number)
#   else:
#     print("ERRO!!! \nNúmero não é PAR")
#   i += 1

#EXERCICIO_(7)

# user = "USER10"
# password = "PASSWORD1234"


# loginUser = input("Digite seu usuário:")
# loginPass = input("Digite sua senha:")

# while loginUser != user and loginPass != password:
#   print("Erro!!!")
#   loginUser = str(input("Digite seu usuário:"))
#   loginPass = str(input("Digite sua senha:"))
# print("LOGIN EFETUADO!")

#EXERCICIO_(8)

# user = "USER10"
# password = "PASSWORD1234"


# loginUser = input("Digite seu usuário (1/3):")
# loginPass = input("Digite sua senha (1/3):")

# i = 2
# while loginUser != user and loginPass != password:
#   if i <= 3:
#     print("Erro!!!")
#     loginUser = str(input(f"Digite seu usuário ({i}/3):"))
#     loginPass = str(input(f"Digite sua senha ({i}/3):"))
#     i += 1
#   else:
#     print("LIMITE DE TENTATIVAS")
#     break 

# if loginUser == user and loginPass == password:
#   print("LOGIN EFETUADO!")

