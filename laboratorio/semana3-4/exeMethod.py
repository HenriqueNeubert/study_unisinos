#EXERCICIO_(1)
# : Crie um método que recebe dois valores val1 e val2 (assuma que serão 
# inteiros). O método deve retornar verdadeiro se val1 for divisível por 
# val2 e falso caso contrário.

# def verif(val1, val2):
#   return val1 % val2 == 0

# verif(2,3)

#EXERCICIO_(2)
# Crie um método chamado maiorValor que recebe 3 valores por parâmetro (assuma
# que serão inteiros) e retorna o maior dos três valores.

# def maiorValor(val1, val2, val3):
#   if val1 > val2 and val1 > val3:
#     return val1
#   if val2 > val1 and val2 > val3:
#     return val2
#   if val3 > val2 and val3 > val1:
#     return val3
  
# maiorValor(3,5,4)

#EXERCICIO_(3)
# Crie um método que recebe um valor por parâmetro (assuma que será inteiro) e
# retorna a soma de todos os valores entre 0 e o valor recebido. Caso o valor 
# seja negativo, o método deve retornar -1.

# def somaValores(number):
#   soma = 0
#   if number < 0:
#     print('NEGATIVO')
#     return -1
#   else:
#     for i in range(0, number + 1):
#       soma += i
#   print(soma)


# somaValores(int(input("Digite um número:")))

#RESPOSTA
# def somaValores(n):
#  soma = 0
#  for i in range(0,n+1): #aqui estamos incluindo o valor n na soma
#  soma += i
#  return soma
#RESPOSTA

#EXERCICIO_(4)
# Crie um método que recebe um valor por parâmetro (assuma que será uma string)
# e retorna a quantidade de letras ou outros caracteres que não sejam espaço 
# que existem neste texto.

# def countLetter(param):
#   count = 0
#   for i in param:
#     if i != " ":
#       count += 1
#       print(i)
#   print(count)

# countLetter(str(input("Digite uma frase:")))

#EXERCICIO_(5)
# Crie um método que recebe uma lista por parâmetro e imprime os elementos da
# lista recebida.
# myList = ["n1", "n2", "n3", "n4", "n5", "n6", "n7"]

# def list(list):
#   for i in myList:
#     print(i)

# list(myList)

#EXERCICIO_(6)
# Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de
# string) e retorna a menor string da lista (com menos caracteres).

# def menorTexto(listaString):
#   menor = -1
#   for i in listaString:
#     if(menor == -1):
#       menor = i
#     elif(len(i) < len(menor)):
#       menor = i
#       return menor
    
# list = ["azul", "vermelho", "preto", "prata"]

# menorTexto(list)

#EXERCICIO_(7)
# Crie um método que recebe dois parâmetros, que serão um inteiro N e uma string
# S (nesta ordem). O método deve imprimir na tela N vezes a string S.

# def calc(n, s):
#   i = 0
#   while i < n:
#     print(s) 
#     i += 1
# calc(5, "azul")

#EXERCICIO_(8)
# : Crie um método que recebe um inteiro X por parâmetro e imprime os valores 
# de 1 até X (inclusive).

# def calc(number):
#   for i in range(1, number + 1):
#     print(i)

# calc(5)

#EXERCICIO_(9)
#  Crie um método que recebe 3 notas por parâmetro e retorna o conceito atingido
# pela média aritmética das notas. Os conceitos são:
# - entre 0.0 e 4.0 (inclusive): conceito "D"
# - entre 4.0 (não incluído) e 7.0 (inclusive): conceito "C"
# - entre 7.0 (não incluído) e 9.0 (inclusive): conceito "B"
# - entre 9.0 (não incluído) e 10.0 (inclusive): conceito "A"
# Caso alguma das notas digitadas seja negativa, retorne o texto "ERRO".

# def notas(nota1, nota2, nota3):
#   if nota1 < 0 or nota2 < 0 or nota3 < 0:
#     print("!!!ERRO!!!")
#   else:
#     media = (nota1 + nota2 + nota3) / 3
#     if media > 0 and media <= 4:
#       print("NOTA (D)", media)
#     elif media > 4 and media <= 7:
#       print("NOTA (C)", media)
#     elif media > 7 and media <= 9:
#       print("NOTA (B)", media)
#     elif media > 9 and media <= 10:
#       print("NOTA (A)", media)

# notas(6, 8, 0)

#EXERCICIO_(10)
# Crie um método que recebe um inteiro por parâmetro e retorna verdadeiro caso
# seja um valor primo e falso caso contrário. Caso o parâmetro seja negativo o 
# método deve retornar falso.