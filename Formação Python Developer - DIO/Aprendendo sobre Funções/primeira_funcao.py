def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

Explicação: 
Claro, este código define três funções diferentes e as chama com diferentes argumentos. Vamos explicar cada parte:

1. `def exibir_mensagem():`: Esta linha define uma função chamada `exibir_mensagem` que não recebe nenhum argumento. Dentro da função, há uma instrução `print` que imprime "Olá mundo!" quando a função é chamada.

2. `def exibir_mensagem_2(nome):`: Aqui, definimos uma função chamada `exibir_mensagem_2` que recebe um argumento chamado `nome`. Dentro da função, há uma instrução `print` que imprime uma mensagem de boas-vindas com o nome fornecido como argumento.

3. `def exibir_mensagem_3(nome="Anônimo"):`: Esta função é semelhante à anterior, mas possui um valor padrão para o argumento `nome`, que é "Anônimo". Isso significa que, se nenhum valor for passado para `nome` quando a função for chamada, será usado o valor padrão "Anônimo".

4. `exibir_mensagem()`: Aqui, estamos chamando a função `exibir_mensagem`, que imprime "Olá mundo!" na saída.

5. `exibir_mensagem_2(nome="Guilherme")`: Esta linha chama a função `exibir_mensagem_2` e passa "Guilherme" como argumento para `nome`. A função então imprime "Seja bem vindo Guilherme!".

6. `exibir_mensagem_3()`: Aqui, estamos chamando a função `exibir_mensagem_3` sem fornecer nenhum argumento. Como nenhum argumento é fornecido, a função usa o valor padrão "Anônimo" para `nome` e imprime "Seja bem vindo Anônimo!".

7. `exibir_mensagem_3(nome="Chappie")`: Finalmente, esta linha chama a função `exibir_mensagem_3` e passa "Chappie" como argumento para `nome`. A função então imprime "Seja bem vindo Chappie!".

Em resumo, o código define três funções que exibem mensagens diferentes e, em seguida, chama cada uma delas com diferentes argumentos para demonstrar seu funcionamento.
