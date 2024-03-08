pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

Explicando as funcionálidades de Dicionários em Python:
1. `pessoa = {"nome": "Guilherme", "idade": 28}`: Aqui, estamos criando um dicionário chamado `pessoa`, que contém duas chaves e seus respectivos valores. A chave `"nome"` tem o valor `"Guilherme"` e a chave `"idade"` tem o valor `28`.
2. `print(pessoa)`: Esta linha imprime o dicionário `pessoa` na saída padrão. Portanto, ao executar esta linha, o output será `{'nome': 'Guilherme', 'idade': 28}`.
3. `pessoa = dict(nome="Guilherme", idade=28)`: Nesta linha, estamos redefinindo a variável `pessoa`, utilizando a função `dict()` para criar um dicionário. Aqui, estamos usando uma forma alternativa de criar um dicionário, especificando os pares chave-valor como argumentos nomeados diretamente dentro da função `dict()`. Isso resulta no mesmo dicionário criado na linha anterior.
4. `print(pessoa)`: Mais uma vez, esta linha imprime o dicionário `pessoa` na saída padrão, que ainda será `{'nome': 'Guilherme', 'idade': 28}`.
5. `pessoa["telefone"] = "3333-1234"`: Aqui estamos adicionando uma nova chave `"telefone"` ao dicionário `pessoa`, com o valor `"3333-1234"`. Isso é feito acessando diretamente a chave `"telefone"` dentro do dicionário `pessoa` e atribuindo um valor a ela.
6. `print(pessoa)`: Esta linha imprime o dicionário `pessoa` após a adição da chave `"telefone"`. Portanto, ao executar esta linha, o output será `{'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'}`. O dicionário agora contém três pares chave-valor.
