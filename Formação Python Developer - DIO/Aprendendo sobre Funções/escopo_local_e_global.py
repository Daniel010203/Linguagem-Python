salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500ruti

Explicação: 
1. `salario = 2000`: Aqui, estamos definindo uma variável chamada `salario` e atribuindo a ela o valor `2000`. Esta variável armazena o salário inicial.
2. `def salario_bonus(bonus):`: Esta linha define uma função chamada `salario_bonus` que aceita um parâmetro `bonus`.
3. `global salario`: Esta linha informa à função que a variável `salario` que está sendo referenciada dentro dela é a mesma variável globalmente definida fora da função. Isso significa que a função tem permissão para modificar o valor da variável `salario` fora de seu escopo local.
4. `salario += bonus`: Nesta linha, estamos aumentando o valor da variável `salario` adicionando o valor do parâmetro `bonus` recebido pela função. Isso aumenta o salário pelo valor do bônus.
5. `return salario`: Esta linha retorna o novo valor do salário após a adição do bônus.
6. `salario_bonus(500)`: Esta linha chama a função `salario_bonus` com um argumento de `500`. Isso significa que um bônus de 500 será adicionado ao salário atual. O resultado desta chamada seria `2500`, pois `2000 + 500 = 2500`.
Assim, ao chamar `salario_bonus(500)`, o salário seria aumentado em 500 e se tornaria `2500`.
