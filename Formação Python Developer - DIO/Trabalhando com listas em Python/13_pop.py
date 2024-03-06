linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

Explicação da função em listas:
Este é um código Python que demonstra o uso do método `pop()` em uma lista.

1. `linguagens = ["python", "js", "c", "java", "csharp"]`: Aqui, uma lista chamada `linguagens` é criada com cinco elementos: "python", "js", "c", "java" e "csharp".

2. `print(linguagens.pop())`: O método `pop()` é chamado sem nenhum argumento, o que significa que ele remove e retorna o último elemento da lista. Portanto, "csharp" é removido da lista e impresso.

3. `print(linguagens.pop())`: Novamente, o método `pop()` é chamado sem nenhum argumento, então o próximo elemento na lista (que agora é "java") é removido e impresso.

4. `print(linguagens.pop())`: Da mesma forma, o método `pop()` é chamado sem nenhum argumento, então o próximo elemento na lista (que agora é "c") é removido e impresso.

5. `print(linguagens.pop(0))`: Aqui, o método `pop()` é chamado com um argumento, o índice 0. Isso significa que o primeiro elemento da lista (que é "python") é removido e impresso.

Então, a saída do código será:

```
csharp
java
c
python
```

Note que `pop()` altera a lista original, removendo os elementos à medida que são chamados.
