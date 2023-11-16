# Crie um algoritmo que leia um número e mostre seu sobro,triplo e a raiz quadrada na tela.
# (\n) faz com que quebre a pagina.
n = int(input("Digite um número: "))
nd = n * 2
nt = n * 3
nq = n **(1/2)
print(print("O número", n, " apresenta o ", nd, "como o dobro \n ", nt, "como o triplo e o \n", nq, "como a raiz quadrada"))


# Outro modelos de algoritmo com o mesmo objetivo.

n = int(input('Digite um número qualquer: '))

dobro = n * 2  
triplo = n * 3 

print(f'O seu número foi: {n}\nO dobro do seu número é: {dobro},')
print(f'Sendo assim o triplo é: {triplo}\ne a raiz quadrada é: {pow(n, 1/2):.2f}')
print('>> FIM <<')
