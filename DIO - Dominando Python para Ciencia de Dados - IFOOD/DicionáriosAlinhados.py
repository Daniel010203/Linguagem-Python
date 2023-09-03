contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"3333-1234"},
    "giovanna@gmail.com":{"nome":"Giovanna","telefone": "3443-2121"},
    "chappie@gmail.com":{"nome": "Chapie","telefone": "3333-7766"},
    "melaine@gmail.com":{"nome": "Melaine","telefone": "3333-9871","extra":{"a":1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)

extra = contatos ["melaine@gmail.com"]["extra"]["a"]

#Podemos usar o comando FOR para fazer a busca geral dentro do dicionário.
for chave,valor in contatos.items():
    print(chave,valor)
