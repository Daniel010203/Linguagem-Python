class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

EXPLICAÇÃO DO CÓDIGO:
O código fornecido é uma demonstração de uma classe Python chamada `Pessoa`, que tem dois métodos especiais e um método estático.

Aqui está uma explicação linha por linha do código original:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```
- Esta parte define a classe `Pessoa` com um construtor `__init__`, que inicializa dois atributos de instância: `nome` e `idade`.

```python
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
```
- Este é um método de classe chamado `criar_de_data_nascimento`. Ele aceita a classe como primeiro argumento (`cls`) e outros argumentos para construir uma instância de `Pessoa`. Ele calcula a idade com base no ano fornecido e retorna uma nova instância de `Pessoa` com o nome e a idade fornecidos.

```python
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
```
- Este é um método estático chamado `e_maior_idade`. Ele verifica se a idade fornecida é maior ou igual a 18 e retorna um valor booleano.

```python
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)
```
- Cria uma nova instância de `Pessoa` usando o método de classe `criar_de_data_nascimento` e imprime o nome e a idade da pessoa.

```python
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
```
- Chama o método estático `e_maior_idade` diretamente da classe `Pessoa` para verificar se a idade é maioridade (>= 18) e imprime os resultados.

Agora, para tornar o código mais limpo e seguir as melhores práticas do Clean Code, podemos fazer algumas melhorias:

1. **Nomenclatura Descritiva**: Use nomes de variáveis mais descritivos para melhorar a legibilidade do código.
2. **Docstrings**: Adicione docstrings para descrever o propósito de cada método.
3. **Clareza e Simplicidade**: Simplifique o código sempre que possível, removendo redundâncias.
4. **Convenção PEP 8**: Mantenha a consistência com as convenções de estilo PEP 8.

Aqui está o código melhorado com essas melhorias:

```python
class Pessoa:
    def __init__(self, nome, idade):
        """Inicializa os atributos da pessoa."""
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_a_partir_de_data_de_nascimento(cls, ano, mes, dia, nome):
        """Cria uma nova pessoa a partir da data de nascimento."""
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def verificar_se_e_maior_idade(idade):
        """Verifica se uma pessoa é maior de idade."""
        return idade >= 18


pessoa = Pessoa.criar_a_partir_de_data_de_nascimento(1994, 3, 21, "Guilherme")
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

print(Pessoa.verificar_se_e_maior_idade(18))
print(Pessoa.verificar_se_e_maior_idade(8))
```

Essas melhorias tornam o código mais legível, fácil de entender e seguir as melhores práticas de programação em Python.
