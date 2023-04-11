import os

##################################
# def verificaPositivo(num):
#   if num >= 0:
#     return True
#   else:
#     return False

# os.system('cls' if os.name == 'nt' else 'clear')
# numero = int(input("Digite:"))
# if verificaPositivo(numero):
#   print("POSITIVO!")
# else:
#   print("NEGATIVO!")
##################################
# def efetuarLogin(user, password):
#   if user.upper() == 'USER01' and password.upper() == 'PASS01':
#     return True
#   else:
#     return False
  
# quant = 0

# while quant < 3:
#   os.system('cls' if os.name == 'nt' else 'clear')
#   usuario = input("Digite Usuário:")
#   senha = input("Digite Senha:")

#   if efetuarLogin(usuario, senha): 
#     print("Login Efetuado!")
#     # quant = 4
#     break
#   else: 
#     quant += 1

# if quant == 3:
#   print("Número Máximo Excedido!")
##################################
# import os

# def menu():
#     opcao = 0
#     while opcao < 1 or opcao > 7:
#         print("-- Opções Disponíveis --")
#         print("1 - Valor por Hora")
#         print("2 - Quantidade de Horas Trabalhadas")
#         print("3 - Salário Bruto")
#         print("4 - INSS")
#         print("5 - Sindicato")
#         print("6 - Salário Líquido")
#         print("7 - Sair")
#         opcao = int(input("Digite a opção desejada: "))

#     return opcao

# os.system('cls' if os.name == 'nt' else 'clear') #Limpa a tela - Win/Linux
# print("--------------------------------------------------------------------------")
# salario_Hora = float(input("Digite o valor recebido por hora R$ "))
# quantidade_Horas = float(input("Digite a quantidade de horas trabalhadas: "))
# print("--------------------------------------------------------------------------")

# #cálculos processamento
# salario_Bruto = salario_Hora * quantidade_Horas
# inss = salario_Bruto * 0.11
# sindicato = salario_Bruto * 0.02
# salario_Liquido = salario_Bruto - inss - sindicato

# opcao_Menu = menu()
# while opcao_Menu != 7: #7 - Sair
#     if opcao_Menu == 1:
#         print("\n-> Valor Recebido por Hora R${:.2f}\n".format(salario_Hora))
#     elif opcao_Menu == 2:
#         print("\n-> Quantidade de Horas Trabalhadas:{}\n".format(quantidade_Horas))
#     elif opcao_Menu == 3:
#         print("\n-> Salário Bruto R${:.2f}\n".format(salario_Bruto))
#     elif opcao_Menu == 4:
#         print("\n-> Valor pago de INSS R${:.2f}\n".format(inss))
#     elif opcao_Menu == 5:
#         print("\n-> Valor pago de Sindicato R${:.2f}\n".format(sindicato))  
#     elif opcao_Menu == 6:
#         print("\n-> Salário Líquido R${:.2f}\n".format(salario_Liquido))
    
#     opcao_Menu = menu()

# print("\nFinalizando...")
