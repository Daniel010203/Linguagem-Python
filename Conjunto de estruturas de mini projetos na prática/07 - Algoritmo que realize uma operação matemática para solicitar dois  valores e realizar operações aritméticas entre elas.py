#Uma operação matemática para solicitar dois  valores e realizar operações aritméticas entre elas.

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print(" A soma é {},\n o produto é {} e \n a divisão é {:.3f}".format(s,m,d),end=" >>>>>>")
print("A divisão inteira {} e potência {}".format(d1, e))

# \n faz o calculo mudar de linha.
# o {:.3} faz o calculo infinito ser finito em quantidade de numeros.
#end após o format faz com que se acrescente algum simbolo após a primeira linha,unindo ela a linha de baixo
