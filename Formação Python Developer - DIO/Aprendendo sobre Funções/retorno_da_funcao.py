def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

Explicação::
1. `def calcular_total(numeros):`: Aqui estamos definindo uma função chamada `calcular_total`, que recebe um parâmetro `numeros`.
2. `return sum(numeros)`: Dentro da função `calcular_total`, estamos utilizando a função `sum()` do Python para somar todos os elementos contidos na lista `numeros` e retornar o resultado dessa soma.
3. `def retorna_antecessor_e_sucessor(numero):`: Aqui estamos definindo outra função chamada `retorna_antecessor_e_sucessor`, que recebe um parâmetro `numero`.
4. `antecessor = numero - 1` e `sucessor = numero + 1`: Dentro da função `retorna_antecessor_e_sucessor`, estamos calculando o antecessor e o sucessor do número recebido como parâmetro.
5. `return antecessor, sucessor`: Esta linha retorna uma tupla contendo o antecessor e o sucessor calculados anteriormente.
6. `print(calcular_total([10, 20, 34]))`: Aqui estamos chamando a função `calcular_total` com uma lista `[10, 20, 34]` como argumento. A função irá somar todos os elementos da lista e retornar o resultado, que será então impresso na saída padrão. No caso, a soma de `10 + 20 + 34` resulta em `64`.
7. `print(retorna_antecessor_e_sucessor(10))`: Aqui estamos chamando a função `retorna_antecessor_e_sucessor` com o argumento `10`. A função calculará o antecessor e o sucessor de `10` e retornará uma tupla contendo esses valores. A tupla `(9, 11)` será então impressa na saída padrão. O antecessor de `10` é `9` e o sucessor é `11`.
