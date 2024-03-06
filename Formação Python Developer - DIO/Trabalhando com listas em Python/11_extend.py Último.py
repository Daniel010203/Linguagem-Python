linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

Explicação da função em listas:
Claro! Vamos analisar o código linha por linha:

```python
linguagens = ["python", "js", "c"]
```

Nesta linha, uma lista chamada `linguagens` é criada e inicializada com três elementos: "python", "js" e "c". Esses elementos representam algumas linguagens de programação.

```python
print(linguagens)  # ["python", "js", "c"]
```

Aqui, o conteúdo da lista `linguagens` é impresso na tela. Isso exibirá os elementos da lista entre colchetes e separados por vírgulas, como mostrado no comentário.

```python
linguagens.extend(["java", "csharp"])
```

Nesta linha, a função `extend()` é chamada na lista `linguagens`. A função `extend()` é usada para adicionar múltiplos elementos a uma lista existente. Neste caso, estamos adicionando os elementos "java" e "csharp" à lista `linguagens`.

```python
print(linguagens)  # ["python", "js", "c", "java", "csharp"]
```

Aqui, novamente, o conteúdo atualizado da lista `linguagens` é impresso na tela. Agora, a lista contém os elementos anteriores ("python", "js", "c") mais os elementos adicionados ("java", "csharp"), como indicado no comentário.

Então, o resultado final é uma lista que contém cinco elementos: "python", "js", "c", "java" e "csharp".
