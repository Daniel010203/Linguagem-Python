class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

Explicação do código:
Este código Python define uma classe chamada `Estudante`. Aqui está uma explicação detalhada do código:

1. **Classe Estudante:**
    - A classe `Estudante` é definida com dois atributos de classe e dois métodos.
    - `escola`: É um atributo de classe que armazena o nome da escola. Por padrão, é definido como "DIO".
    - `__init__(self, nome, matricula)`: Este é o construtor da classe `Estudante`. Ele é chamado quando um novo objeto `Estudante` é criado. Ele inicializa os atributos `nome` e `matricula` do objeto com os valores passados durante a instanciação.
    - `__str__(self)`: Este é o método especial que retorna uma representação de string do objeto `Estudante`. Ele retorna uma string formatada contendo o nome, a matrícula e o nome da escola do estudante.

2. **Função mostrar_valores:**
    - Esta é uma função que aceita um número variável de argumentos. Ela itera sobre todos os objetos passados como argumentos e os imprime.

3. **Instanciando objetos:**
    - `aluno_1`, `aluno_2` e `aluno_3` são instâncias da classe `Estudante`. Eles são criados passando o nome e a matrícula como argumentos para o construtor.

4. **Chamando a função mostrar_valores:**
    - No primeiro chamado para `mostrar_valores`, `aluno_1` e `aluno_2` são passados como argumentos. Isso imprimirá os detalhes desses dois alunos, incluindo seus nomes, matrículas e a escola (que é "DIO" por padrão).
    - Em seguida, a escola é alterada para "Python".
    - No segundo chamado para `mostrar_valores`, `aluno_1`, `aluno_2` e `aluno_3` são passados como argumentos. Isso imprimirá os detalhes desses três alunos. Agora, todos os alunos mostrarão a nova escola como "Python", pois o atributo de classe `escola` foi alterado.

Em resumo, o código cria uma classe `Estudante` com alguns atributos e métodos. Em seguida, ele instancia objetos dessa classe e demonstra como acessar e modificar os atributos de classe e instância.
