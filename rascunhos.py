#idade = 19
#altura = 1.98
#name = "Nome"

#nome = input("Digite seu Nome: ")
#print("Seu nome é:",nome)

#preco = float(input("Digite o valor: "))
#print("O preço é:",preco)

#precoProduto1 = float(input("Digite o preço do primeiro produto: "))
#precoProduto2 = float(input("Digite o preço do segundo produto: "))

#precoTotal = precoProduto1 + precoProduto2

#print("O valor total é:", precoTotal)

#preco = float(input("Digite o preço:"))
#desconto = preco * 0.1
#print("Valor do desconto:",desconto)

#preco = float(input("Digite o preço:"))
#desconto = preco * 0.1
#print("Valor do desconto:",preco-desconto)

#valor1 = float(input("Digite o primeiro valor:"))
#valor2 = float(input("Digite o segundo valor:"))
#valor3 = float(input("Digite o terceiro valor:"))

#media = (valor1 + valor2 + valor3) / 3
#print("Media dos valores:", media)

########################################################################
#IMPRESSÃO BÁSICA
print("Hello, world!")
#SOLICITANDO DADOS
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso:"))
#VERIFICA TIPO DE DADOS
type(nome)
#QUEBRA DE LINHA
print("Hello\nWorld")
#FORMATAÇÃO
#UTILIZANDO (.format)
#format= outra maneira de trabalhar 
#com imprerssão de dados em variaveis
print("Ola {} sua idade é {} anos.".format(nome,idade))
print("Inteiro: {:d}".format(12354))
#saída: 12354
print("Zero à esquerda: {:04d}".format(25))
#saída: 0025
print("Casas decimais: {:.2f}".format(2.545445))
#saída: 2.54

#IF - ELSE - ELIF
number = 5
if number > 0:
	print("POSITIVO")
elif number == 0:
	print("0")
else:
  print("NEGATIVO")

#WHILE
i = 0
while i < 100:
	print("valor de i:", i)
	i += 1
	if i == 32:
		break 
		#brak=para 

op = int(input("Digite 3 para sair:"))
while op != 3:
	print("Você digitou", op, "\nVocê não saiu.")
	op = int(input("Digite 3 para sair:"))
	
#FOR
semana = [
"SEGUNDA",
"TERÇA",
"QUARTA",
"QUINTA",
"SEXTA",
"SÁBADO",
"DOMINGO"
]

for dia in semana:
	print(dia)

#ex2
for num in range(1,6):
	print(num)
	
#CRIAR LISTA
#cria uma lista vazia
lista = []
#para adicionar um item 
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
for item in lista:
	print(item)
	
#METODOS
#metodo
def meuMetodo(cor):
	print(cor)#imprime a string "AZUL"
#chama o metodo
#"AZUL é o parâmetro"
meuMetodo("AZUL")

def soma(a,b):
	return a+b
soma(2,3) 













