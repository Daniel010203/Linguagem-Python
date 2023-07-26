#Quando usamos o import math o código importa todas as funcionalidades da função math.
import math
numero=int(input("Digite um numero: "))
raiz = math.sqrt(numero)
print("A raiz de {:.3f} é igual a {:.3f}".format(numero,raiz))

#Quando desejamos usar somente uma função dentro do de math. usamos o from na frente.
from math import sqrt,floor
numero=int(input("Digite um numero: "))
raiz = sqrt(numero) # Não precisamo mais usar o math aqui,pois já foi definido lá encima a função.
print("A raiz de {:.3f} é igual a {:.3f}".format(numero,raiz))