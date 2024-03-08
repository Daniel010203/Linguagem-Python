contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear()
print(contatos)  # {}

Explicando as funcionálidades de Dicionários em Python:
1. `contatos = { "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}, "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}, }`: Nesta linha, estamos definindo um dicionário chamado `contatos`. Cada chave do dicionário é um endereço de e-mail e o valor correspondente é outro dicionário contendo o nome e o telefone de uma pessoa.
2. `contatos.clear()`: Aqui, estamos utilizando o método `clear()` para remover todos os itens do dicionário `contatos`. Isso esvazia completamente o dicionário, removendo todas as chaves e valores.
3. `print(contatos)`: Esta linha imprime o dicionário `contatos` após a operação de limpeza. Como o dicionário foi esvaziado anteriormente, a saída será `{}`, indicando que o dicionário está vazio, sem nenhum par chave-valor.
Em resumo, o código define um dicionário chamado `contatos` contendo informações de contato associadas a endereços de e-mail. Em seguida, utiliza o método `clear()` para remover todos os itens desse dicionário, resultando em um dicionário vazio que é impresso na saída.
