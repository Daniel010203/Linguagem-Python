matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

Explicação desta função em listas:
Este código demonstra operações básicas com listas multidimensionais em Python, conhecidas como matrizes. Aqui está a explicação linha por linha:
1. `matriz = [...]`: Esta linha define uma matriz como uma lista de listas em Python. Cada lista interna representa uma linha na matriz. Neste caso, a matriz é uma lista contendo três listas internas, onde cada uma representa uma linha da matriz.
2. `print(matriz[0])`: Isso imprime a primeira linha da matriz. Em Python, a indexação de listas começa em 0, então `matriz[0]` acessa a primeira lista interna na matriz.
3. `print(matriz[0][0])`: Isso imprime o primeiro elemento da primeira linha da matriz. Portanto, `matriz[0][0]` acessa o primeiro elemento da primeira lista interna.
4. `print(matriz[0][-1])`: Isso imprime o último elemento da primeira linha da matriz. Em Python, índices negativos contam a partir do final da lista. Portanto, `matriz[0][-1]` acessa o último elemento da primeira lista interna.
5. `print(matriz[-1][-1])`: Isso imprime o último elemento da última linha da matriz. Aqui, o uso de índices negativos acessa a última lista interna (linha) da matriz e, em seguida, o último elemento dessa lista.
Essencialmente, esse código demonstra como acessar elementos específicos em uma matriz bidimensional em Python, tanto pelo índice da linha quanto pelo índice da coluna.
