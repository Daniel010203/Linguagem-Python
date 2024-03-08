def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)

Explicação : 
Esse código define uma função chamada `exibir_poema` que aceita um argumento obrigatório (`data_extenso`) e qualquer número de argumentos posicionais (`args`) e argumentos de palavra-chave (`kwargs`). Vou explicar o que cada parte faz:

1. `def exibir_poema(data_extenso, *args, **kwargs):`: Esta linha define a função `exibir_poema`. Ela possui três parâmetros: `data_extenso`, que é obrigatório, `*args`, que coleta argumentos posicionais em uma tupla, e `**kwargs`, que coleta argumentos de palavra-chave em um dicionário.

2. `texto = "\n".join(args)`: Aqui, estamos convertendo os argumentos posicionais (`args`) em uma única string, onde cada argumento é separado por uma quebra de linha (`\n`). Isso é feito usando o método `join()` para concatenar os elementos da tupla `args` com uma quebra de linha entre eles.

3. `meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])`: Nesta linha, estamos criando uma string contendo os argumentos de palavra-chave (`kwargs`) formatados como pares "chave: valor", onde cada par é separado por uma quebra de linha (`\n`). Estamos iterando sobre os itens do dicionário `kwargs` usando o método `items()`, formatando cada par chave-valor com a primeira letra da chave em maiúsculo (`chave.title()`) seguida pelo valor.

4. `mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"`: Aqui, estamos concatenando o argumento `data_extenso`, o texto e os metadados em uma única string `mensagem`. Entre cada seção, estamos incluindo duas quebras de linha para separar visualmente os diferentes componentes do poema.

5. `print(mensagem)`: Esta linha imprime a mensagem composta na saída padrão.

No exemplo fornecido, a função `exibir_poema` é chamada com um poema ("Zen of Python") como primeiro argumento, seguido por várias linhas do poema como argumentos posicionais, e informações adicionais do autor e do ano como argumentos de palavra-chave. A função então imprime o poema com os metadados formatados adequadamente.
