nome = "Daniel"
idade = 34
profissão = "Programador"
linguagem = "Python"

print("Olá, meu nome é %s eu tenho %s minha profissão é %s e a linguagem de programação que utilizo é a %s." % (nome,idade,profissão,linguagem))
# Não costumamos utilizar mais o %,pois torna o código mais dificil de se ler.

print("Olá, meu nome é {} eu tenho {} minha profissão é {} e a linguagem de programação que utilizo é a {}.".format (nome,idade,profissão,linguagem))
# Podemos utilizar o .format para interpolar as strings de acordo com as variáveis. Neste método temos que seguir exatamente a ordem das palavras em cada situação.

print("Olá, meu nome é {0} eu tenho {1} minha profissão é {2} e a linguagem de programação que utilizo é a {3}.".format (nome,idade,profissão,linguagem))
# Podemos utilizar o .format para interpolar as strings de acordo com as variáveis. Neste método temos que seguir exatamente a ordem das palavras em cada situação.
# Neste formato,podemos utilizar a enumeração dos itens para atender de acordo com as variáveis citadas em suas respectivas ordem. Isso acontece muito em códigos extensos.

print("Olá, meu nome é {nome} eu tenho {idade} minha profissão é {profissão} e a linguagem de programação que utilizo é a {linguagem}.".format (nome=nome,idade=idade,profissão=profissão,linguagem=linguagem))
# Este formato também é muito utilizado para se identificar itens dentro da variável. Lembrando que a primeira strig é o item e o segundo é o nome da variável.ex: nome(Daniel=nome(variável).

#print("Olá, meu nome é {nome} eu tenho {idade} minha profissão é {profissão} e a linguagem de programação que utilizo é a {linguagem}.".format(**pessoa))
# Utilizamos este item para incluir strings de um dicionário e nele já constam todas as informações necessárias para o preenchimento da string completa.

print(f"Olá, meu nome é {nome} eu tenho {idade} minha profissão é {profissão} e a linguagem de programação que utilizo é a {linguagem}.")
# Este formato é muito utilizado,pois facilita o preenchimento das strigs com somente um item na variável.

PI = 3.14159

print(f"O valor de PI:{PI:.2f}")
# O {.2f} indica quantas casas decimenas que quero ter na resposta após o ponto.
print(f"O valor de PI:{PI:10.2f}")
# O {10.} indica quantas casas decimais eu quero de espaço antes do ponto.
