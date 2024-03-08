contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)

Explicação da funcionálidade em Dicionários de Python:
1. `contatos = { ... }`: Aqui estamos definindo um dicionário chamado `contatos`. Em Python, os dicionários são coleções de pares chave-valor, onde cada chave é única e mapeada para um valor. Neste caso, as chaves são os endereços de e-mail e os valores são dicionários que contêm informações adicionais sobre cada contato, como nome e telefone.
2. `del contatos["guilherme@gmail.com"]["telefone"]`: Esta linha remove a chave "telefone" do dicionário associado ao endereço de e-mail "guilherme@gmail.com". O operador `del` é usado para excluir uma chave de um dicionário.
3. `del contatos["chappie@gmail.com"]`: Esta linha remove completamente o elemento associado à chave "chappie@gmail.com" do dicionário `contatos`.
4. `print(contatos)`: Esta linha imprime o dicionário `contatos` atualizado após as operações de exclusão. O dicionário agora contém apenas os contatos restantes, sem os detalhes de telefone do contato "guilherme@gmail.com" e sem o contato "chappie@gmail.com".
Em resumo, o código removeu o número de telefone do contato "guilherme@gmail.com" e excluiu completamente o contato "chappie@gmail.com" do dicionário `contatos`, resultando em um novo dicionário contendo apenas os contatos restantes.
