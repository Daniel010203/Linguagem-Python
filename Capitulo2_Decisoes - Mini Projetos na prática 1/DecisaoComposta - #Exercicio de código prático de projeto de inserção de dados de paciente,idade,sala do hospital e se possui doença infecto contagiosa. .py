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

#Este código em Python é um programa simples para direcionar um paciente para uma sala de hospital com base em seu nome,
# idade e se há suspeita de doença infectocontagiosa. Vou explicar cada parte do código:
# 1. O programa começa exigindo ao usuário que insira o nome do paciente, a idade e se há suspeita de doença infectocontagiosa. Os valores são lidos a partir da entrada padrão (teclado) usando a função `input`. ```python nome = input("Digite o nome: ") idade = int(input("Digite a idade: ")) doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiante?").upper() ```
# 2. O programa converte a resposta para a suspeita de doença infecciosa em letras secretas usando `.upper()`. Isso garante que a verificação seja insensível a autoridades e subsidiárias.
# 3. Em