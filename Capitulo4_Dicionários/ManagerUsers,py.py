print("Olá, informe abaixo se deseja inserir,pesquisar,excluir,listar ou sair.")
print(input("O que deseja realizar: "))
usuario = {}
opcao = input("O que deseja realizar?\n +"
              "<I> - Para inserir um usuário\n"+
              "<P> - Para pesquisar um usuário\n"+
              "<E> - Para excluir um usuário\n" +
              "<L> - Para Listar um usuário: ").upper()
while opcao =="I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao =="I":
        chave = input("Digite o login: ").upper()
        nome = input("Digite o nome: ").upper()
        data = input("Digite a ultima data de acesso: ")
        estacao = input("Digite a ultima estação acesssada: ").upper()
    opcao = input("O que deseja realizar?\n + "
                  "<I> = Para inserir um usuário\n +"
                  "<P>  - Para pesquisar um usuário\n +"
                  "<E> - Para excluir um usuário\n +"
                  "<L> - Para listar um usuário: ").upper()
