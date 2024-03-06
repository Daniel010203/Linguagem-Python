carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


Explicação da função em tuplas:
Claro! Vamos analisar o código passo a passo:

1. Primeiro, criamos uma **tupla** chamada `carros` com três elementos: `"gol"`, `"celta"` e `"palio"`.

2. Em seguida, usamos um **loop `for`** para iterar sobre cada elemento da tupla `carros`. O loop executa o bloco de código abaixo para cada carro na tupla:
   ```python
   for carro in carros:
       print(carro)
   ```
   Isso imprime cada carro em uma linha separada:
   ```
   gol
   celta
   palio
   ```

3. Além disso, utilizamos o **loop `for` com a função `enumerate()`** para obter tanto o índice quanto o valor de cada carro na tupla. O bloco de código abaixo é executado para cada carro:
   ```python
   for indice, carro in enumerate(carros):
       print(f"{indice}: {carro}")
   ```
   Isso imprime o índice seguido pelo nome do carro:
   ```
   0: gol
   1: celta
   2: palio
   ```

Em resumo, o código demonstra como iterar sobre os elementos de uma tupla e também como obter o índice associado a cada elemento usando a função `enumerate()`. Espero que isso tenha esclarecido! 😊
