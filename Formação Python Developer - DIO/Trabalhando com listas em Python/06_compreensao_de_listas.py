# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

Explicação da função em listas:
Este código Python demonstra duas funcionalidades comuns: filtrar uma lista com base em uma condição e modificar os valores da lista original.
1. Filtrar lista:
   O primeiro trecho de código cria uma lista chamada `numeros`, que contém alguns números inteiros. Em seguida, ele usa uma sintaxe conhecida como compreensão de lista para criar uma nova lista chamada `pares`. Dentro da compreensão de lista, ele percorre cada elemento da lista `numeros` com o loop `for numero in numeros`. Para cada elemento, ele verifica se o número é par usando a expressão `if numero % 2 == 0`. Se o número for par, ele é incluído na lista `pares`. Finalmente, a lista `pares` é impressa.
2. Modificar valores:
   O segundo trecho de código também começa com a lista `numeros` contendo alguns números inteiros. Em seguida, ele usa outra compreensão de lista para criar uma nova lista chamada `quadrado`. Neste caso, ele percorre cada elemento da lista `numeros` com o loop `for numero in numeros` e eleva ao quadrado cada elemento usando a expressão `numero**2`. O resultado é uma lista contendo os quadrados de cada número na lista original `numeros`. Essa lista `quadrado` é então impressa.
Em resumo, o primeiro trecho de código filtra os números pares da lista `numeros`, enquanto o segundo trecho modifica os valores da lista `numeros` elevando cada número ao quadrado.
