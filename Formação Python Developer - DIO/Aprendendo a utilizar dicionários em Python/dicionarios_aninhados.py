contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

Explicação:
1. `contatos = { ... }`: Aqui estamos criando um dicionário chamado `contatos`. Um dicionário em Python é uma estrutura de dados que mapeia chaves a valores. Neste caso, as chaves são endereços de e-mail e os valores são dicionários aninhados contendo informações sobre os contatos.
2. `"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}`: Este é um exemplo de um item no dicionário `contatos`. A chave é `"guilherme@gmail.com"` e o valor é um dicionário contendo duas chaves: `"nome"` com valor `"Guilherme"` e `"telefone"` com valor `"3333-2221"`. Este padrão se repete para cada contato.
3. `telefone = contatos["giovanna@gmail.com"]["telefone"]`: Aqui estamos acessando o valor associado à chave `"giovanna@gmail.com"` no dicionário `contatos`. Isso nos retorna outro dicionário contendo informações sobre o contato com o endereço de e-mail `"giovanna@gmail.com"`. Em seguida, estamos acessando a chave `"telefone"` neste dicionário interno para obter o número de telefone de Giovanna. Esse número é então atribuído à variável `telefone`.
4. `print(telefone)`: Por fim, estamos imprimindo o número de telefone de Giovanna na saída padrão.
Em resumo, o código extrai e imprime o número de telefone do contato com o endereço de e-mail `"giovanna@gmail.com"` do dicionário `contatos`.
