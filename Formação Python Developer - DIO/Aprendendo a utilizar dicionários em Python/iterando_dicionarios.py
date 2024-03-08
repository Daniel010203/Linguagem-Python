contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)

Explicação:
1. `contatos = { ... }`: Aqui estamos definindo um dicionário chamado `contatos`. Em Python, um dicionário é uma estrutura de dados que mapeia chaves para valores. No caso presente, as chaves são os endereços de e-mail e os valores são dicionários que contêm informações sobre cada contato, como nome e telefone.
2. `for chave in contatos: ...`: Este é um loop `for` que itera sobre as chaves do dicionário `contatos`. Em cada iteração, a variável `chave` contém a chave atual do dicionário.
3. `print(chave, contatos[chave])`: Dentro do loop, estamos imprimindo a chave atual seguida pelo valor correspondente no dicionário `contatos`.
4. `print("=" * 100)`: Esta linha imprime uma linha de 100 sinais de igual. Isso é apenas para separar visualmente os dois loops na saída.
5. `for chave, valor in contatos.items(): ...`: Aqui estamos usando o método `items()` do dicionário para iterar sobre os pares chave-valor do dicionário `contatos`. Em cada iteração, a variável `chave` recebe a chave atual e a variável `valor` recebe o valor correspondente.
6. `print(chave, valor)`: Dentro deste segundo loop, estamos imprimindo a chave atual seguida pelo valor correspondente no dicionário `contatos`.
Resumindo, o código imprime as informações de contato contidas no dicionário `contatos` duas vezes: primeiro, utilizando um loop simples sobre as chaves do dicionário e, em seguida, utilizando o método `items()` para iterar sobre os pares chave-valor do dicionário.
