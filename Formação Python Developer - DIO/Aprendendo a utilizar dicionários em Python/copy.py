contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}

Explicação da funcionálidade de Dicionários em Python:
1. `contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}`: Nesta linha, estamos criando um dicionário chamado `contatos`. Ele tem uma única entrada, onde a chave é o e-mail "guilherme@gmail.com" e o valor é outro dicionário contendo informações sobre o contato, como o nome "Guilherme" e o telefone "3333-2221".
2. `copia = contatos.copy()`: Aqui, estamos criando uma cópia superficial do dicionário `contatos` e atribuindo-a à variável `copia`. Uma cópia superficial significa que estamos criando um novo dicionário que contém as mesmas chaves e valores que o dicionário original, mas os valores em si (como dicionários internos) não são copiados. Em vez disso, eles são referenciados no novo dicionário.
3. `copia["guilherme@gmail.com"] = {"nome": "Gui"}`: Nesta linha, estamos modificando o valor associado à chave "guilherme@gmail.com" no dicionário `copia`. Estamos substituindo o dicionário existente por outro dicionário com o nome "Gui".
4. `print(contatos["guilherme@gmail.com"])`: Aqui, estamos imprimindo o valor associado à chave "guilherme@gmail.com" no dicionário `contatos`. Como o dicionário `contatos` não foi alterado após a cópia, a saída será `{"nome": "Guilherme", "telefone": "3333-2221"}`.
5. `print(copia["guilherme@gmail.com"])`: Aqui, estamos imprimindo o valor associado à chave "guilherme@gmail.com" no dicionário `copia`. Como modificamos o valor desta chave na cópia, a saída será `{"nome": "Gui"}`.
