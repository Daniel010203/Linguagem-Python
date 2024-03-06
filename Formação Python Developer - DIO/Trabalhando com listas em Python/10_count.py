cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

Explicação da função em listas:
Este código em Python demonstra o uso do método `count()` em listas. Aqui está uma explicação detalhada das funcionalidades do código:

```python
# Define uma lista chamada cores com quatro elementos
cores = ["vermelho", "azul", "verde", "azul"]

# Imprime o número de vezes que "vermelho" aparece na lista cores
print(cores.count("vermelho"))  # Saída: 1

# Imprime o número de vezes que "azul" aparece na lista cores
print(cores.count("azul"))  # Saída: 2

# Imprime o número de vezes que "verde" aparece na lista cores
print(cores.count("verde"))  # Saída: 1
```

Explicação:

- `cores.count("vermelho")`: Este comando conta o número de vezes que o elemento "vermelho" aparece na lista `cores`. Como "vermelho" aparece apenas uma vez na lista, a saída será `1`.
- `cores.count("azul")`: Este comando conta o número de vezes que o elemento "azul" aparece na lista `cores`. Como "azul" aparece duas vezes na lista, a saída será `2`.
- `cores.count("verde")`: Este comando conta o número de vezes que o elemento "verde" aparece na lista `cores`. Como "verde" aparece apenas uma vez na lista, a saída será `1`.

O método `count()` retorna o número de ocorrências de um determinado elemento em uma lista.
