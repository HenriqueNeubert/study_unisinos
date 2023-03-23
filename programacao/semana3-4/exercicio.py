#EXERCICIO_(1)
  #Crie um programa que recebe um inteiro pelo teclado e imprime se 
  # ele é par ou ímpar.  
  
# number = int(input("Digite um número:"))
# if number % 2 == 0 :
#   print("PAR")
# else:
#   print("IMPAR")
     
################################RESPOSTA
# numero = int(input("Digite um inteiro:"))
# if numero < 0:
# print("ERRO: número negativo")
# elif numero == 0:
# print("ERRO: número é zero")
# elif numero % 2 == 0:
# print("Número",numero,"é par!")
# else:
# print("Número",numero,"é ímpar!")
################################RESPOSTA

#EXERCICIO_(2)
  # Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime 
  # o valor de A dividido por B. Entretanto, se o valo de B for 0, imprima uma 
  # mensagem de erro e não faça a divisão.

# a = int(input("Digite um número (A):"))
# b = int(input("Digite um número (B):"))

# if b != 0:
#   resultado = a / b
#   print("Resultado:", resultado)
# else:
#   print("ERRO:", b)

#EXERCICIO_(3)
  # Crie um programa que recebe um valor inteiro referente a um determinado ano. 
  # Imprima na tela se o ano informado é bissexto ou não (para simplificar, você 
  # pode utilizar apenas a informação de o ano é divisível por 4 ou não).

# ano = int(input("Digite um ano:")) 
# if ano / 4 == 0:
#   print("O ano é bissexto:", ano)
# else:
#   print("O ano não é bissexto:", ano)

################################RESPOSTA
# ano = int(input("Digite um ano:"))
# if ano % 4 == 0:
#  print("O ano",ano,"é bissexto.")
# else:
#  print("O ano",ano,"não é bissexto.")
################################RESPOSTA

#EXERCICIO_(4)
  # Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e 
  # imprime na tela se será necessário ou não realizar o Grau C (considere o sistema 
  # de avaliação da Unisinos, sendo o GA valendo 30% e o GB valendo 70%). Caso algum
  # valor informado seja negativo, informe uma mensagem de erro e não realize o 
  # cálculo.

# #30%
# notaA = int(input("Digite sua nota do grau A:")) 
# #70%
# notaB = int(input("Digite sua nota do grau B:")) 

# if notaA < 0 or notaB < 0:
#   print("Erro ao informar a nota.")
# else:
#   result = ((notaA * 30 / 100) + (notaB * 70 / 100)) 
#   print(result)

################################RESPOSTA
# grauA = float(input("Digite a nota do GA:"))
# grauB = float(input("Digite a nota do GB:"))
# if grauA >= 0 and grauB >= 0:
# notaFinal = 0.3 * grauA + 0.7 * grauB
# if notaFinal >= 6:
#  print("Não precisa de Grau C =)")
# else:
#  print("Precisa de Grau C =(")
# else:
# print("Uma das notas é negativa. Não é possível realizar
# o cálculo.")
################################RESPOSTA

#EXERCICIO_(5)
  # Crie um programa que solicita que o usuário digite uma letra e imprime na tela
  # se a letra é uma vogal ou uma consoante.

# letra = str(input("Digite uma letra:")) 

# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#   print("VOGAL")
# else:
#   print("CONSOANTE")
 
#EXERCICIO_(6)
  # O que é um parâmetro de entrada de um método?

# São valores que o método necessita receber para poder realizar sua função. Os
# parâmetros de entrada são definidos dentro dos parêntesis do método e
# permitem que o método receba informações externas de quem o invocou.

#EXERCICIO_(7)
  # O que é o retorno de um método?

# É o valor que o método dará como resposta a quem o invocou após realizar sua
# função. Quando um método retorna algum valor, quem invocou o método
# receberá este valor e pode utilizá-lo na continuidade do programa.
 
#EXERCICIO_(8)
  # Utilizando while, crie um programa que imprime os números de 0 a 1000. 

# number = 0
# while number <= 1000:
#   print(number) 
#   number += 1 

#EXERCICIO_(9)
  # Utilizando while, crie um programa que imprime os números pares de 0 a 2000.

# number = 0

# while number <= 2000:
#     print(number)
#     number += 2
 
#EXERCICIO_(10)
  # Utilizando while, crie um programa que imprime os números de 0 a 1000 em 
  # ordem decrescente (ou seja, de 1000 a 0).

# number = 1000

# while number >= 0:
#   print(number)
#   number -= 1
 
#EXERCICIO_(11)
  # Utilizando while, crie um programa que solicita para o usuário que ele digite 10
  #  valores inteiros. Ao final, imprima a soma de todos os valores digitados. 

################################RESPOSTA
# cont = 0
# soma = 0
# while cont < 10:
#  valor = int(input("Digite um valor: "))
#  soma += valor
#  cont += 1
# print("Soma dos valores digitados:",soma)
################################RESPOSTA

#EXERCICIO_(12)
  # Comparando os comandos de repetição for e while, em quais ocasiões é mais comum 
  # a utilização de um ou de outro?

  # O comando while geralmente é mais utilizado quando não sabemos a quantidade de 
  # repetições que nosso código fará. Por exemplo, “enquanto o usuário não acertar 
  # o usuário e a senha, peça novamente”. Já o comando for é mais utilizado quando 
  # sabemos o número de iterações a realizar. Por exemplo, “o usuário possui 5 
  # tentativas para acertar o usuário e a senha”.
 
#EXERCICIO_(13)
  # Utilizando for, crie um programa imprime na tela os valores de 1 
  # a 100 (incluindo o 1 e o 100).

# for i in range(1, 101):
#   print(i)
 
#EXERCICIO_(14)
  # Utilizando for,crie um programa que imprime a tabuada de um número inteiro 
  # digitado pelo usuário.

# number = int(input("Digite um número:"))
# i = number

# for number in range(1, 11):
#   print(number, "*", i, "=", number * i)

################################RESPOSTA
# num = int(input("Digite o valor para calcular a tabuada:"))
# for i in range(1,11):
#   print(num,"x",i,"=",(num*i))
################################RESPOSTA
 
#EXERCICIO_(15)
  # Crie um programa que permita que o usuário crie sua lista de compras. 
  # Primeiramente, solicite que ele informe quantos produtos serão adicionados
  # na lista. Depois disto, peça para que o usuário digite os produtos que ele 
  # vai comprar, e armazene em uma lista. Ao final, imprima a lista de compras 
  # do usuário.

# quantidade = 3
# produto = 1
# listaCompras = []

# while produto <= quantidade:
#   item = input("Digite o nome do produto:")
#   listaCompras.append(item)
#   produto += 1
# print(listaCompras)

################################RESPOSTA
# quant = int(input("Quantos produtos você terá na lista?"))
# listaDeCompras = []
# for i in range(0,quant):
#   listaDeCompras.append(input("Digite o produto:"))
#   print("Lista de compras:")
# for i in listaDeCompras:
#   print(i)
################################RESPOSTA
