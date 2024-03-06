linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

Explicação da função em listas:

Claro, vamos analisar o código linha por linha:

```python
linguagens = ["python", "js", "c", "java", "csharp"]
```

Nesta linha, uma lista chamada `linguagens` é criada, contendo cinco strings que representam diferentes linguagens de programação.

```python
print(linguagens.index("java"))  # 3
```

Aqui, o método `index()` é usado para encontrar o índice da primeira ocorrência do elemento especificado dentro da lista `linguagens`. Ele retorna o índice onde "java" está localizado dentro da lista. No caso, "java" está na posição 3 da lista `linguagens`, então o valor impresso será 3.

```python
print(linguagens.index("python"))  # 0
```

Nesta linha, o método `index()` é novamente usado para encontrar o índice da primeira ocorrência do elemento especificado dentro da lista `linguagens`. Como "python" está na primeira posição da lista, o índice retornado será 0. Portanto, o valor impresso será 0.
