linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

Explicação da função em listas:
Este código Python demonstra o uso do método `remove()` em uma lista. Vamos analisar linha por linha:

1. `linguagens = ["python", "js", "c", "java", "csharp"]`: Aqui, uma lista chamada `linguagens` é criada, contendo cinco strings que representam diferentes linguagens de programação.

2. `linguagens.remove("c")`: Esta linha remove a primeira ocorrência do elemento "c" da lista `linguagens`. No caso, "c" representa a linguagem C.

3. `print(linguagens)`: Esta linha imprime o conteúdo da lista `linguagens` após a remoção do elemento "c".

4. Com base na operação de remoção realizada, o resultado impresso será `["python", "js", "java", "csharp"]`, pois a linguagem "c" foi removida da lista original.
