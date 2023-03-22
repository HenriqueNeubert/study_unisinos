# ENTRADA
num_1 = int(input("Digite um número:"))
num_2 = int(input("Digite um número:"))
#PROCESSAMENTO
soma = num_1 + num_2
sub = num_1 - num_2
mult = num_1 * num_2
div = num_1 / num_2
div_int = num_1 // num_2
resto = num_1 % num_2
exponenciacao = num_1 ** num_2 #or pow(num_1, num_2)
#SAIDA
print("Soma:{}".format(soma))
print("Sub:{}".format(sub))
print("mult:{}".format(mult))
print("div:{:.2f}".format(div))
print("div_int:{}".format(div_int))
print("exponenciacao:{}".format(exponenciacao))