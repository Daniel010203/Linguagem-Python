# Depois de print(" - colocamos o "\t" ou "\n" para acrescentar uma tabulação antes no numero.
# em "numero=numero+5" eu determino de quantos em quantos numeros será a sequencia até chegar ao 100.Podemos utilizar a alinha numero+=5 também.
numero=int(input("Digite um numero: "))
while numero<100:
    print("\t" + str(numero))
    numero=numero+5
print("Laço encerrado ....")