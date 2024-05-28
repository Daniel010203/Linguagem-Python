lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

Explicação da função em listas:
Este código demonstra o uso de fatiamento (slicing) em listas em Python. Aqui está uma explicação linha por linha:
1. `lista = ["p", "y", "t", "h", "o", "n"]`: Cria uma lista chamada `lista` com os caracteres "p", "y", "t", "h", "o", "n".
2. `print(lista[2:])`: Imprime todos os elementos da lista a partir do índice 2 até o final. Resultado: `["t", "h", "o", "n"]`.
3. `print(lista[:2])`: Imprime todos os elementos da lista do início até o índice 2 (exclusivo). Resultado: `["p", "y"]`.
4. `print(lista[1:3])`: Imprime os elementos da lista do índice 1 (inclusive) até o índice 3 (exclusivo). Resultado: `["y", "t"]`.
5. `print(lista[0:3:2])`: Imprime os elementos da lista do índice 0 até o índice 3 (exclusivo), pulando de 2 em 2. Resultado: `["p", "t"]`.
6. `print(lista[::])`: Imprime todos os elementos da lista. Esta é uma maneira de copiar a lista inteira. Resultado: `["p", "y", "t", "h", "o", "n"]`.
7. `print(lista[::-1])`: Imprime todos os elementos da lista em ordem reversa, começando do último elemento até o primeiro, com um passo de -1. Resultado: `["n", "o", "h", "t", "y", "p"]`.
Essas são as funcionalidades básicas de fatiamento de listas em Python, que permitem acessar e manipular partes específicas de uma lista de acordo com os índices fornecidos.
