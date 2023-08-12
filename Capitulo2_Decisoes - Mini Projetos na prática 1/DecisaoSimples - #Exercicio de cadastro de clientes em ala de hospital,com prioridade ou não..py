#Exercicio de cadastro de clientes em ala de hospital,com prioridade ou não.Decisão simples.

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="Não"
if idade>65:
    prioridade="SIM"
print("O paciente " + nome +" possui atendimento prioritario? " + prioridade)