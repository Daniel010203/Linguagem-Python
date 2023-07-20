#Exercicio de código prático de projeto de código de inserção de dados de paciente,idade,sala do hospital e se possui doença infecto contagiosa.

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiante?").upper()
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paicente será direcionada para a sala amarela - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa=="SIM":
    print("O paicente será direcionada para a sala amarela - SEM prioridade")
elif idade>=65 and doenca_infectocontagiosa=="NÃO":
    print("O paicente será direcionada para a sala branca - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa=="NÃO":
    print("O paicente será direcionada para a sala branca - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")
