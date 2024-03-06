linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

Explicação da função em listas:
Este código Python demonstra o uso do método `sort()` em listas, permitindo ordená-las de diferentes maneiras.

1. **Ordenação padrão**:
   ```python
   linguagens = ["python", "js", "c", "java", "csharp"]
   linguagens.sort()  # Ordena em ordem alfabética crescente
   print(linguagens)
   ```
   Este trecho de código ordena a lista `linguagens` em ordem alfabética crescente. Após a execução do método `sort()`, a lista será `["c", "csharp", "java", "js", "python"]`.

2. **Ordenação reversa**:
   ```python
   linguagens = ["python", "js", "c", "java", "csharp"]
   linguagens.sort(reverse=True)  # Ordena em ordem alfabética decrescente
   print(linguagens)
   ```
   Este trecho de código ordena a lista `linguagens` em ordem alfabética decrescente. Após a execução do método `sort()`, a lista será `["python", "js", "java", "csharp", "c"]`.

3. **Ordenação com base no comprimento das strings**:
   ```python
   linguagens = ["python", "js", "c", "java", "csharp"]
   linguagens.sort(key=lambda x: len(x))  # Ordena com base no comprimento das strings
   print(linguagens)
   ```
   Aqui, a lista `linguagens` é ordenada com base no comprimento das strings. O argumento `key=lambda x: len(x)` especifica que a ordenação deve ser feita com base no comprimento das strings. Após a execução, a lista será `["c", "js", "java", "python", "csharp"]`, onde as strings são ordenadas pelo número crescente de caracteres.

4. **Ordenação reversa com base no comprimento das strings**:
   ```python
   linguagens = ["python", "js", "c", "java", "csharp"]
   linguagens.sort(key=lambda x: len(x), reverse=True)  # Ordena com base no comprimento das strings em ordem decrescente
   print(linguagens)
   ```
   Neste último trecho, a lista `linguagens` é ordenada com base no comprimento das strings, mas em ordem decrescente. O resultado será `["python", "csharp", "java", "js", "c"]`, onde as strings são ordenadas pelo número decrescente de caracteres.
