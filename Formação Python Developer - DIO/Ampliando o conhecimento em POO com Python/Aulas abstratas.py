from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)


EXPLICAÇÃO DO CÓDIGO:

Este código Python é um exemplo de como usar a abstração e herança de classes para criar um sistema de controle remoto genérico, com implementações específicas para diferentes dispositivos controlados, como uma TV e um Ar Condicionado.

Aqui está uma explicação do código:

1. Importação do módulo `ABC` do pacote `abc`: Isso é necessário para definir classes abstratas.
2. Definição da classe abstrata `ControleRemoto`: Esta classe define métodos abstratos para ligar, desligar e uma propriedade abstrata para a marca do dispositivo.
3. Definição da classe concreta `ControleTV`, que herda de `ControleRemoto`: Esta classe fornece implementações concretas para os métodos `ligar`, `desligar` e a propriedade `marca` específica para uma TV da marca "Philco".
4. Definição da classe concreta `ControleArCondicionado`, que também herda de `ControleRemoto`: Esta classe fornece implementações concretas semelhantes para os métodos `ligar`, `desligar` e a propriedade `marca`, mas especificamente para um Ar Condicionado da marca "LG".
5. Instância de objetos `controle` de ambas as classes `ControleTV` e `ControleArCondicionado`, chamando seus métodos `ligar`, `desligar` e imprimindo suas marcas.

Agora, vamos melhorar o código seguindo as práticas do CLEAN CODE:

1. **Nomenclatura Descritiva**: Use nomes descritivos para classes, métodos e variáveis para tornar o código mais legível.
2. **Documentação**: Adicione documentação explicativa sempre que necessário para ajudar os outros desenvolvedores a entender o propósito das classes e métodos.
3. **Organização**: Mantenha o código organizado e claro, seguindo uma estrutura lógica.
4. **Evite Comentários Óbvios**: Se o código é autoexplicativo, evite comentários redundantes.
5. **Evite Repetição de Código**: Se houver trechos de código repetidos, considere encapsulá-los em funções ou métodos.
6. **Use f-strings**: Para formatação de strings, é preferível usar f-strings em vez do método `.format()` para melhorar a legibilidade.

Aqui está o código com melhorias seguindo essas práticas:

```python
from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    MARCA = "Philco"

    def ligar(self):
        print("Ligando a TV...")
        print("TV ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!")

    @property
    def marca(self):
        return self.MARCA


class ControleArCondicionado(ControleRemoto):
    MARCA = "LG"

    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ar Condicionado ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Ar Condicionado desligado!")

    @property
    def marca(self):
        return self.MARCA


def testar_controle(ControleCls):
    controle = ControleCls()
    controle.ligar()
    controle.desligar()
    print(f"Marca: {controle.marca}\n")


if __name__ == "__main__":
    testar_controle(ControleTV)
    testar_controle(ControleArCondicionado)
```

Principais melhorias:

- Utilização de constantes para as marcas.
- Uso de f-strings para formatação de strings.
- Adição de uma função de teste `testar_controle()` para evitar repetição de código ao testar os controles.
- Estruturação do código principal em um bloco `if __name__ == "__main__":` para permitir reutilização do módulo.
