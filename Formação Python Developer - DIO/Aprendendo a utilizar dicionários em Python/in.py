contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)

Explicação:
1. `contatos = {...}`: Aqui estamos criando um dicionário chamado `contatos`. Um dicionário em Python é uma estrutura de dados que mapeia chaves para valores. Cada chave é única e associada a um valor. No caso, as chaves são os endereços de e-mail e os valores são dicionários que contêm informações sobre os contatos, como nome e telefone.
2. `resultado = "guilherme@gmail.com" in contatos`: Aqui estamos verificando se a chave "guilherme@gmail.com" existe no dicionário `contatos`. O operador `in` é utilizado para essa verificação, e o resultado da verificação é atribuído à variável `resultado`. Neste caso, como a chave existe, `resultado` será `True`.
3. `print(resultado)`: Esta linha imprime o valor da variável `resultado`. Portanto, a saída será `True`.
4. `resultado = "megui@gmail.com" in contatos`: Aqui estamos verificando se a chave "megui@gmail.com" existe no dicionário `contatos`. Como essa chave não existe, `resultado` será `False`.
5. `print(resultado)`: Esta linha imprime o valor da variável `resultado`. Portanto, a saída será `False`.
6. `resultado = "idade" in contatos["guilherme@gmail.com"]`: Aqui estamos verificando se a chave "idade" existe no dicionário associado à chave "guilherme@gmail.com". Como essa chave não existe nesse dicionário específico, `resultado` será `False`.
7. `print(resultado)`: Esta linha imprime o valor da variável `resultado`. Portanto, a saída será `False`.
8. `resultado = "telefone" in contatos["giovanna@gmail.com"]`: Aqui estamos verificando se a chave "telefone" existe no dicionário associado à chave "giovanna@gmail.com". Como essa chave existe nesse dicionário específico, `resultado` será `True`.
9. `print(resultado)`: Esta linha imprime o valor da variável `resultado`. Portanto, a saída será `True`.
