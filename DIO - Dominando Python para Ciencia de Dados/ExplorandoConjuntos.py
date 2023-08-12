# set forma uma coleção que não possui objetos repetidos.
#não será em ordem.
carros = set(("palio","gol","celta","palio"))
print(carros)

#a função set com {} já faz essa seleção automaticamente para não ter objetos repetidos.
linguagens = {"python","php","ruby","php","python","Java"}
print(linguagens)

#Para poder acessar o conteudo de set,deve-se transforma-lo em uma lista.
numeros = {1,2,3,2}
print(numeros[0])

numeros = list(numeros)
print(numeros[0])

#Para percorrer toda a lista,utilizamos o For.
carros = {"gol","celta","palio"}
for carro in carros:
    print(carro)

#Função enumerate permite saber qual o indice do objeto dentro do laço For.
carros = {"gol","celta","palio"}
for indice,carro in enumerate(carros):
    print(f"{indice}:{carro}")

# a função {}UNION, permite a união dos conjuntos num unico.
conjunto_a = {1,2}
conjunto_b = {3,4}
print(conjunto_a.union(conjunto_b)) # o resultado será {1,2,3,4}

# a função {}intersection faz a intersecção entre conjuntos citados.
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.intersection(conjunto_b)) # o resultado será {2,3}

# a função {}difference trás a diferença entre conjuntos.
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.difference(conjunto_b)) # o resultado será {1}
print(conjunto_b.difference(conjunto_a)) # o resultado será {4}

# a função {}symemtric_difference coleta todos os dados que não se misturam nos conjuntos.
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.symmetric_difference(conjunto_b)) # o resultado será {1,4}
print(conjunto_b.difference(conjunto_a)) # o resultado será {4}

# a função {}issubset indica se todos os itens dentro de um conjunto estão ou não dentro do outro.
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}
print(conjunto_a.issubset(conjunto_b)) # False
print(conjunto_b.issubset(conjunto_a)) # True

# a função {}add faz a adição de conteudo dentro de conjuntos.
sorteio = {1,23}
print(sorteio.add(25)) #{1,23,25}
print(sorteio.add(42)) #{1,23,25,42}
print(sorteio.add(25)) #{1,23,25,42} o  item 25 que já existia foi ignorado.

# a função {}clear faz a limpeza completa da lista/conjunto.
sorteio = {1,23}
print(sorteio.clear()) #{1,23}

# a função {}copy é copiará todo o conjunto.
sorteio = {1,23}
print(sorteio.copy()) #{1,23}

# a função {}discard faz o descarte do item selecionado na lista.
numeros = {1,2,3,4,5,6,8,9}
print(numeros.discard(1))
print(numeros.discard(35))
# numeros #{2,3,4,5,6,8,9} # removeu o 1 e como não tinha o 35 ele seguiu em frente sem problemas.

# a função {}pop sempre irá remover o valor a frente da lista.
numeros = {1,2,3,4,5,6,8,9}
print(numeros.pop()) #0
print(numeros.pop()) #1
print(numeros)

# a função {}remove faz a remoção do item selecionado e caso esse item não conste na lista, ele sinaliza erro.
numeros = {1,2,3,4,5,6,8,9}
print(numeros.remove(1))
print(numeros.remove(35))

# a função {}len serve para tirar o tamanho do nosso conjunto todo.
numeros = {1,2,3,4,5,6,8,9}
len(numeros)
print(1 in numeros) # true
print(20 in numeros) #false


