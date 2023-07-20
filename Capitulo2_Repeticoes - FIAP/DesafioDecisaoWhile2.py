#Exercicio de código de identificação de cliente,idade e doença infecto contagiosa.Decisão while 2.

nome=input("Digite seu nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

#PRIMEIRO PROBLEMA A SER RESOLVIDO
while doenca_infectocontagiosa!="SIM" and doenca_infectocontagiosa!="NÃO":
    print("Digite SIM ou NÃO")
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

if doenca_infectocontagiosa=="SIM":
    print("Enacminhe o paciente para a sala AMARELA")
else:
    print("Encaminhe o paciente para a sala BRANCA")

#SEGUNDO PROBLEMA A SER RESOLVIDO
while idade>=65:
    print("Paciente COM prioridade")
else:
    print("Paciente SEM prioridade")

genero=input("Digite o gênero do paciente: ").upper()
while genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM" and gravidez!="NÃO":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")


