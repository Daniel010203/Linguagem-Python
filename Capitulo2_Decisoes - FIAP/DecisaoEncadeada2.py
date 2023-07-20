#Exercicio de código de cadastro de clientes em ala de hospital,com doença infecto contagiosa.Decisão encadeada 2.

nome=input("Digite seu nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

#PRIMEIRO PROBLEMA A SER RESOLVIDO

if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para a sala AMARELA")
elif doenca_infectocontagiosa=="NÃO":
    print("Encaminhe o paciente para a sala BRANCA")

#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade>=65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")