#ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS,
# MOSTRANDO NA TELA A MENSAGEM:
# O PRIMEIRO VALOR É MAIOR.
# O SEGUNDO VALOR É MAIOR.
# NÃO EXISTE VALOR MAIOR,OS DOIS SAO IGUAIS.
valor_um=int(input("Digite um valor: "))
valor_dois=int(input("Digite outro valor: "))
if valor_um> valor_dois:
    print("O primeiro valor é maior!")
elif valor_um<valor_dois:
    print("O segundo valor é maior!")
else:
    print("Não existe valor maior,pois os dois são numeros iguais!")
