matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

Explicação da função de tuplas:
Claro! Vamos analisar o código passo a passo:

1. Primeiro, criamos uma **matriz** (que é uma tupla de tuplas) chamada `matriz`. Ela contém três tuplas internas, cada uma com três elementos.
2. `print(matriz[0])`: Isso imprime a primeira tupla da matriz, que é `(1, "a", 2)`.
3. `print(matriz[0][0])`: Aqui, acessamos o primeiro elemento da primeira tupla, que é `1`.
4. `print(matriz[0][-1])`: Isso acessa o último elemento da primeira tupla, que é `2`.
5. `print(matriz[-1][-1])`: Aqui, acessamos o último elemento da última tupla, que é `"c"`.
Em resumo, o código demonstra como acessar elementos específicos dentro de uma matriz (ou tupla de tuplas). Espero que isso tenha esclarecido! 😊
