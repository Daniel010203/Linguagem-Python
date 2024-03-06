linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

Explicação da função em listas:
Este código em Python demonstra o uso da função `sorted()` para classificar uma lista de strings com base no comprimento das strings. Vou explicar as funcionalidades do código linha por linha:

```python
linguagens = ["python", "js", "c", "java", "csharp"]
```

Nesta linha, uma lista chamada `linguagens` é criada e preenchida com cinco strings que representam algumas linguagens de programação.

```python
print(sorted(linguagens, key=lambda x: len(x)))
```

Aqui, a função `sorted()` é usada para ordenar a lista `linguagens` com base no comprimento de cada elemento. O parâmetro `key` é uma função lambda que é usada para extrair o comprimento de cada elemento (`x`) da lista. A função `len(x)` retorna o comprimento da string `x`. Isso significa que a lista será ordenada de acordo com o comprimento das strings em ordem crescente. O resultado é impresso usando `print()`.

```python
# Saída: ["c", "js", "java", "python", "csharp"]
```

A saída mostraria a lista ordenada com base no comprimento das strings, do menor para o maior: `["c", "js", "java", "python", "csharp"]`.

```python
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
```

Nesta linha, a mesma função `sorted()` é usada, mas o parâmetro `reverse=True` é adicionado. Isso inverte a ordem de classificação, tornando-a do maior para o menor comprimento. Portanto, a lista resultante será ordenada com base no comprimento das strings em ordem decrescente. O resultado é impresso usando `print()`.

```python
# Saída: ["python", "csharp", "java", "js", "c"]
```

A saída mostraria a lista ordenada com base no comprimento das strings, do maior para o menor: `["python", "csharp", "java", "js", "c"]`.
