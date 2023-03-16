import math
#EXERCICIO_(1)
#Faça um Programa que mostre a mensagem "Alo mundo" na tela. 
# print("HELLO WORLD")

# #EXERCICIO_(2)
# # Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# number = int(input("Digite um número:"))
# print(f"Seu número é {number}")

#EXERCICIO_(3)
# Faça um Programa que peça dois números e imprima a soma.

# number1 = int(input("Digite um número:"))
# number2 = int(input("Digite um número:"))
# print(f"A soma é: {number1 + number2}")

#EXERCICIO_(4)
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# nota1 = int(input("Digite a nota:"))
# nota2 = int(input("Digite a nota:"))
# nota3 = int(input("Digite a nota:"))
# nota4 = int(input("Digite a nota:"))

# print(f"A média é : {(nota1 + nota2 + nota3 + nota4) / 4}")

#EXERCICIO_(5)
# Faça um Programa que converta metros para centímetros.
# metros = float(input("Digite um valor (m):"))
# print(f"...sendo assim, {metros} metros são equivalentes a {metros*100} centimetros")

#EXERCICIO_(6)
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# raio = int(input("Digite um número:"))
# pi = 3.14
# area = (2 * pi) * raio
# print("A área do círculo é:", area)

#EXERCICIO_(7)
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 
# altura = int(input("Digite a altura do quadrado:"))
# area = altura ** 2 
# print(f"A área do quadrado é {area}, e o seu dobro é {((altura ** 2) * 2)}.")

#EXERCICIO_(8)
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# hora = float(input("Digite quanto você ganha por hora:"))
# horasMes= float(input("Digite quantas horas você trabalhou no mês:"))

# salario = hora * horasMes 
# print(salario)

#EXERCICIO_(9)
# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e 
#mostre a temperatura em graus Celsius.

#     C = 5 * ((F-32) / 9). 
#70 > 21.11
# fahremheit = int(input("Digite a temperatura (fa):"))
# celsius = 5 * ((fahremheit - 32) / 9)
# print("A temperatura em celsius é%.2f " %celsius)

#EXERCICIO_(10)
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre 
#em graus Fahrenheit. 

# celsius = int(input("Digite a temperatura (celsius):"))
# #f = 1.8 c+32
# fahremheit = int(1.8 * 21.11 + 32) 
# print("A temperatura em Fahrenheit é ", fahremheit)

#EXERCICIO_(11)
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# int1 = int(input("Digite um número"))
# int2 = int(input("Digite um número"))
# float1 = float(input("Digite um número"))
# int1 = 5
# int2 = 3
# float1 = 3.2
#o produto do dobro do primeiro com metade do segundo .
# totalA = (int1 * 2) * (int2 / 2) 
# print("O produto do dobro do primeiro com metade do segundo:", totalA)
# #a soma do triplo do primeiro com o terceiro.
# totalB = int1 * 3 + float1
# print("A soma do triplo do primeiro com o terceiro:", totalB)
# #o terceiro elevado ao cubo. 
# totalC = float1 * float1 * float1
# print("O terceiro elevado ao cubo: %.2f" %totalC)

#EXERCICIO_(12)
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
#calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
# altura = float(input("Digite sua altura:")) 
# altura = 1.80

# pesoIdeal = 72.7 * altura - 58
# print("%.2f" %pesoIdeal,"kg")

#EXERCICIO_(13)
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
#que calcule seu peso ideal, utilizando as seguintes fórmulas:

#height = float(input("Digite sua altura:"))
# height = 1.75
#Para homens: (72.7*h) - 58
# idealMan = 72.7 * height - 58
# print("O peso ideal do senhor seria: %.2f" %idealMan, "kg")
#Para mulheres: (62.1*h) - 44.7 
# idealWoman = 62.1 * height - 44.7
# print("O peso ideal da senhora seria: %.2f" %idealWoman, "kg")

#EXERCICIO_(14)
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
#  o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça 
# um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar
# na variável excesso a quantidade de quilos além do limite e na variável multa o 
# valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens 
# adequadas.
# Limite 50kg
# Multa 4 p/kg

# pesoPeixe = float(input("Kilos de peixe:"))
# # pesoPeixe = 51

# if pesoPeixe > 50:
#   excedido = pesoPeixe - 50
#   multa = excedido * 4
#   print("Sua pesca de hoje excedeu em", excedido, "kg, você deverá pagar uma multa estipulada em %.2f" %multa, "R$" )
# else:
#   print("Sua pesca de hoje não excedeu os nossos limites de peso.")

#EXERCICIO_(15)
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#  trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#  sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
# 5% para o sindicato, faça um programa que nos dê:

# iRenda = 11
# inss = 8 
# sindicato = 5

# hora = float(input("Digite o valor de 1 hora:"))
# horasMes = float(input("Digite a quantidade de horas trabalhadas:"))
# #     salário bruto.
# salarioBruto = hora * horasMes
# print("Salário bruto:", salarioBruto)
# #     quanto pagou ao INSS.
# valorInss = salarioBruto * inss / 100
# print("Quanto pagou ao INSS:", valorInss)
# #     quanto pagou ao sindicato.
# valorSindicato = salarioBruto * sindicato / 100
# print("Quanto pagou ao sindicato:", valorSindicato)
# #     o salário líquido.
# valorRenda = salarioBruto * iRenda / 100
# salarioLiquido = salarioBruto - valorSindicato - valorInss - valorRenda
# print("O salário líquido:", salarioLiquido)
# #     calcule os descontos e o salário líquido, conforme a tabela abaixo:
# print('RESUMO', )
# print(' + Salário Bruto : R$', salarioBruto)
# print('- IR (11%) : R$', valorRenda)
# print('- INSS (8%) : R$', valorInss)
# print('- Sindicato ( 5%) : R$', valorSindicato)
# print('= Salário Liquido : R$', salarioLiquido)

#EXERCICIO_(16)
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 
# litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
# a serem compradas e o preço total.

# area = float(input("Metros quadrados:"))
# valorLata = 80
# litrosLata = 18
# clienteLitros = area / 3
# clienteLatas = clienteLitros / litrosLata

# print("Quantidade de latas: %.2f" %clienteLatas)
# # add (import math) ao topo do arquivo
# print("Quantidade de latas (arredondado):",  math.ceil(clienteLatas))
# valorTotal = clienteLatas * valorLata
# print("Valor total: %.2f " %valorTotal, "R$")

#EXERCICIO_(17)
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
#  é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

area = float(input("Metros quadrados:"))
lata = input("Tamanho da lata (G/P):")
valorLataG = 80
valorLataP = 25
litrosLataG = 18
litrosLataP = 3.6
clienteLitros = area / 6
clienteLatasG = clienteLitros / litrosLataG
clienteLatasP = clienteLitros / litrosLataP
# Informe ao usuário as quantidades de tinta a serem compradas e os 
# respectivos preços em 3 situações:


if lata == "G" or lata == "g":
  #comprar apenas latas de 18 litros;
  print("Quantidade de latas: %.2f" %clienteLatasG)
        # add (import math) ao topo do arquivo
  print("Quantidade de latas (arredondado):",  math.ceil(clienteLatasG))
  valorTotal = math.ceil(clienteLatasG) * valorLataP
  print("Valor total: %.2f R$" %valorTotal)

if lata == "P" or lata == "p":
  #comprar apenas galões de 3,6 litros;
  print("Quantidade de latas: %.2f" %clienteLatasP)
        # add (import math) ao topo do arquivo
  print("Quantidade de latas (arredondado):",  math.ceil(clienteLatasP))
  valorTotal = math.ceil(clienteLatasP) * valorLataP
  print("Valor total: %.2f R$" %valorTotal)

# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
# considere latas cheias. 

#EXERCICIO_(18)
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
# aproximado de download do arquivo usando este link (em minutos). 

# tamanho = 2000
# velocidade = 8 
# minuto = velocidade * 60
# total = tamanho / minuto
# print(minuto, "mbpm")
# print("%.2f" %total,"min")





