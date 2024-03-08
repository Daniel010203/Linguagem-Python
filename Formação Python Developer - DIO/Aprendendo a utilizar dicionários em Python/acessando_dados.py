dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

Explicando as funcionálidades de Dicionários em Python:

1. `dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}`: Aqui estamos criando um dicionário chamado `dados`. Um dicionário em Python é uma estrutura de dados que mapeia chaves a valores. Neste dicionário, estamos associando as chaves "nome", "idade" e "telefone" aos valores "Guilherme", 28 e "3333-1234", respectivamente.
2. `print(dados["nome"])`: Esta linha imprime o valor associado à chave "nome" no dicionário `dados`. Portanto, a saída será `"Guilherme"`.
3. `print(dados["idade"])`: Aqui estamos imprimindo o valor associado à chave "idade" no dicionário `dados`. A saída será `28`.
4. `print(dados["telefone"])`: Esta linha imprime o valor associado à chave "telefone" no dicionário `dados`. A saída será `"3333-1234"`.
5. `dados["nome"] = "Maria"`: Estamos atualizando o valor associado à chave "nome" no dicionário `dados` para "Maria".
6. `dados["idade"] = 18`: Aqui estamos atualizando o valor associado à chave "idade" no dicionário `dados` para 18.
7. `dados["telefone"] = "9988-1781"`: Estamos atualizando o valor associado à chave "telefone" no dicionário `dados` para "9988-1781".
8. `print(dados)`: Esta linha imprime o dicionário `dados` após as atualizações. Portanto, a saída será `{"nome": "Maria", "idade": 18, "telefone": "9988-1781"}`, que reflete as alterações feitas nos valores associados às chaves "nome", "idade" e "telefone".
