contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)

Explicação :
1. `contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}`: Aqui, estamos criando um dicionário chamado `contatos` com uma entrada inicial. Esta entrada consiste em uma chave `"guilherme@gmail.com"` associada a um dicionário que contém informações sobre um contato, incluindo o nome e o telefone.
2. `contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})`: Esta linha atualiza o dicionário `contatos`, substituindo a entrada existente para o e-mail "guilherme@gmail.com" por um novo dicionário. O novo dicionário tem apenas uma entrada para a chave `"nome"`, que foi atualizada para "Gui".
3. `print(contatos)`: Aqui, estamos imprimindo o dicionário `contatos` após a atualização. Como resultado da atualização anterior, a saída será `{'guilherme@gmail.com': {'nome': 'Gui'}}`, pois agora o dicionário `contatos` contém apenas a entrada atualizada para o e-mail "guilherme@gmail.com".
4. `contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})`: Esta linha adiciona uma nova entrada ao dicionário `contatos`. Agora, o dicionário `contatos` terá uma entrada adicional para o e-mail "giovanna@gmail.com", associada a um dicionário que contém informações sobre o contato da Giovanna, incluindo seu nome e telefone.
5. `print(contatos)`: Aqui, estamos imprimindo o dicionário `contatos` novamente após a segunda atualização. Agora, o dicionário `contatos` terá duas entradas: uma para "guilherme@gmail.com" e outra para "giovanna@gmail.com", cada uma com suas respectivas informações de contato. A saída será `{'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}`.
