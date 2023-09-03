# Nos dicionários,podemos criar listas para preencher/modificar os valores dentro dos mesmos.

dados = {"nome": "Guilherme", "idade": 28,"telefone":"3333-1234"}
dados["nome"] #Guilherme
dados["idade"] #28
dados["telefone"] #3333-1234

dados["nome"] = "Maria" #O nome Maria subscreveu o nome Guilherme.
dados["idade"] = 18 # a idade 18 subscreveu a idade 28
dados["telefone"] = 9988-1781 # o telefone 9988-1781 subscreveu o 3333-1234

print(dados) # No dicionário dados, a a lista nome possui o valor Maria,a idade 18 e o telefone 8207.

# O {}fronkeys cria chaves para voce utilizar no seu dicionário.
dict.fromkeys(["nome","telefone"])
dict.fromkeys(["nome","telefone"],"vazio") #Nesta opção podemos incluir uma informação as chaves no lugar da palavra vazio.
# TODOS AS FUNÇÕES EM "EXPLORANDO CONJUNTOS" podem ser utilizadas dentro de dicionários.

# o comando {}get busca na chave informada o conteudo e caso não tenha,pode informar outra informação a seguir.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-2112"}
}
contatos["chave"] #keyError
contatos.get("chave") #None
contatos.get("chave", {}) #{}
contatos.get("guilherme@gmail.com",{}) #{"guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-2112"}

# o comando {}keys retorna somente a chave do dicionário.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-2112"}
}
contatos.keys()

# o comando {}popitem faz a busca da chave informada.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-2112"}
}
contatos.popitem()

# o comando {}setdefault serve para inserir um valor dentro do seu dicionário.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-2112"}
}
contatos.setdefault("nome")

# o comando {}update permite atulizar o dicionário com novos dados.
# o comando {}values retorna somente os valores das chaves.
# o comando {}in verifica itens dentro do dicionário.
# o comando {}del elimina itens dentro do dicionário.
