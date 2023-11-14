#Faça um programa que leia um número inteiro e
# mostre na tela seu sucessor e antecessor de forma automática.

n1 = int(input("Dígite um número: "))
n_a= n1 - 1
n_s= n1 + 1
print("O número ",n1, "tem como antecessor o ",n_a," e como sucessor o ",n_s)

#Outro Exemplo de como
#n = int(input('Digite um número: '))
#print('---' * 22)
#print('Analizando o numero {} seu sucessor é {} e antecessor é {}'.format(n, n+1, n-1))
#print('---' * 22)